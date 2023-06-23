from rest_framework import mixins
from rest_framework import generics

from .serializer import ReviewSerializer
from ....models import Review


class ReviewListApiView(generics.ListAPIView):
    '''get all reviews of all contents'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ContentReviewListApiView(generics.ListAPIView):
    '''get all reveiws of specific cotnent given the content id'''
    serializer_class = ReviewSerializer

    def get_queryset(self):
        content_pk = self.kwargs['pk']
        return Review.objects.filter(content=content_pk)


class ReviewCreateApiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailsApiVeiw(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ContentReviewDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer

    def get_object(self):
        # we first get the cotnent
        content_id = self.kwargs['content_pk']
        review_id = self.kwargs['review_pk']
        review = Review.objects.get(pk=review_id, content=content_id)
        return review
