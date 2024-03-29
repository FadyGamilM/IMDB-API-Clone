from rest_framework.views import APIView
from .serializer import ContentSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ....models import Content
from ..review.serializer import ReviewSerializer
from rest_framework import generics
from ....models import Review, Content
from rest_framework.exceptions import ValidationError
#######################################################################################################
# class ContentListApiView(APIView):
#     def get(self, request: Request):
#         # 1. we need find all content instances
#         # 2. serialize them
#         # 3. return the response with proper status code
#         contents = Content.objects.all()
#         serializer = ContentSerializer(contents, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# => Refacotr to generic view
class ContentListApiView(generics.ListAPIView):
    '''list all cotnents'''
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
#######################################################################################################

#######################################################################################################
# class ContentCreateApiView(APIView):
#     def post(self, request: Request):
#         # 1. first we need to serialize the data from the request
#         # 2. check if the data is serialized and valid
#         # 3. persist the created instance by calling .save()
#         # 4. return the proper response
#         serilizer = ContentSerializer(request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serilizer.errors(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# => Refacotr to generic view
class ContentCreateApiView(generics.CreateAPIView):
    '''create new content'''
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
# ######################################################################################################


# ######################################################################################################
# class ContentDetailsActionsApiView(APIView):
#     def get(self, request: Request, pk: int):
#         # 1. try to found the resource with given pk
#         # 2. serialize the found resource
#         # 3. return the response
#         try:
#             content = Content.objects.get(pk=pk)
#         except Content.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         serialized_data = ContentSerializer(content)
#         return Response(serialized_data, status=status.HTTP_200_OK)

#     def put(self, request: Request, pk: int):
#         # 1. try to found the resource with given pk
#         # 2. serialize the found resource
#         # 3. update the data by calling save
#         # 4. return the proper response
#         try:
#             content = Content.objects.get(pk=pk)
#         except Content.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ContentSerializer(instance=content, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response({"error": "couldn't update the resource"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def delete(self, request: Request, pk: int):
#         # 1. try to found the resource with given pk
#         # 2. serialize the found resource
#         # 3. delete the data by calling delete
#         # 4. return the proper response
#         try:
#             content = Content.objects.get(pk=pk)
#         except Content.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         content.delete()
#         return Response(data="deleted", status=status.HTTP_204_NO_CONTENT)

# => Refacotr to generic view
class ContentDetailsActionsApiView(generics.RetrieveUpdateDestroyAPIView):
    '''get | update | delete specific content'''
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
#######################################################################################################


class ContentReviewListApiView(generics.ListAPIView):
    '''get all reveiws of specific cotnent given the content id'''
    serializer_class = ReviewSerializer

    def get_queryset(self):
        content_pk = self.kwargs['pk']
        return Review.objects.filter(content=content_pk)


class ContentReviewDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_object(self):
        # we first get the cotnent
        content_id = self.kwargs['content_pk']
        review_id = self.kwargs['review_pk']
        review = Review.objects.get(pk=review_id, content=content_id)
        return review


class ContentReviewCreateApiView(generics.CreateAPIView):
    # specify the serializer that the view will work with
    serializer_class = ReviewSerializer
    # specify which model the view will operate on
    queryset = Review.objects.all()

    # we specified the serializer class above, so when we pass a serialzier to 
    # the method, we mean the serialzier of the review resource not the content resource
    def perform_create(self, review_serializer):
        '''
            1. get the primary key of the content
            2. get the user who created this request
            3. get the review that is made by this user and for this content (if exists)
            4. if this review exists raise a ValidationError
            5. if this review doesn't exist, then call the reviewSerializer.save() to save this review as a new one
            6. update the content metadata such as avg_rating and total_num_of_reviews
        '''
        # 1. get the content via content passed id
        content_pk = self.kwargs['content_pk']
        content = Content.objects.get(pk=content_pk)

        # 2. check that the reviewer didn't review on this content before
        #  ➜  get the user who initiated this request
        review_owner = self.request.user
        review_of_this_content_by_this_user = Review.objects.filter(
            content=content_pk, reviewer=review_owner)
        if review_of_this_content_by_this_user.exists():
            raise ValidationError("this user reviewed on this content before")
        
        # update the content metadata
        content.total_num_of_reviews += 1
        print('total count -> ',content.total_num_of_reviews)
        content.avg_rating = (content.avg_rating * (content.total_num_of_reviews - 1) + review_serializer.validated_data['rating']) / content.total_num_of_reviews
        print('avg rating -> ', content.avg_rating)
        print('new rating -> ', review_serializer.validated_data['rating'])
        content.save()

        # 2. save the new review by specifying the content and the owner
        review_serializer.save(content=content, reviewer=review_owner)
