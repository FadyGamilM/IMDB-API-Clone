from rest_framework import mixins
from rest_framework import generics

from .serializer import ReviewSerializer
from ....models import Review


class ReviewListApiView(generics.ListAPIView):
    '''get all reviews of all contents'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateApiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailsApiVeiw(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
