from rest_framework.views import APIView
from .serializer import StreamingPlatformSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ....models import StreamingPlatform
from rest_framework import generics

#######################################################################################################
# class StreamingPlatformListApiView(APIView):
#     def get(self, request: Request):
#         # 1. we need find all streaming platforms instances
#         # 2. serialize them
#         # 3. return the response with proper status code
#         resources = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(
#             resources, many=True, context={'request': request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# => Refacotr to generic view
class StreamingPlatformListApiView(generics.ListAPIView):
    '''list all streaming platforms'''
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
#######################################################################################################


#######################################################################################################
# class StreamingPlatformCreateApiView(APIView):
#     def post(self, request: Request):
#         # 1. first we need to serialize the data from the request
#         # 2. check if the data is serialized and valid
#         # 3. persist the created instance by calling .save()
#         # 4. return the proper response
#         serilizer = StreamingPlatformSerializer(request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serilizer.errors(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# => Refacotr to generic view
class StreamingPlatformCreateApiView(generics.CreateAPIView):
    '''create new streaming platform'''
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
#######################################################################################################


#######################################################################################################
# class StreamingPlatformDetailsActionsApiView(APIView):
#     def get(self, request: Request, pk: int):
#         # 1. try to found the resource with given pk
#         # 2. serialize the found resource
#         # 3. return the response
#         try:
#             resource = StreamingPlatform.objects.get(pk=pk)
#         except resource.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamingPlatformSerializer(resource)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request: Request, pk: int):
#         # 1. try to found the resource with given pk
#         # 2. serialize the found resource
#         # 3. update the data by calling save
#         # 4. return the proper response
#         try:
#             resource = StreamingPlatform.objects.get(pk=pk)
#         except resource.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamingPlatformSerializer(
#             instance=resource, data=request.data)
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
#             resource = StreamingPlatform.objects.get(pk=pk)
#         except StreamingPlatform.DoesNotExist:
#             return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
#         resource.delete()
#         return Response(data="deleted", status=status.HTTP_204_NO_CONTENT)

# => Refacotr to generic view
class StreamingPlatformDetailsActionsApiView(generics.RetrieveUpdateDestroyAPIView):
    '''get | update | delete an existing platform'''
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer

#######################################################################################################
