from rest_framework import mixins
from rest_framework import generics

from .serializer import ReviewSerializer
from ....models import Review


class ReviewListApiView(generics.ListAPIView):
    '''get all reviews of all contents'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateApiView(generics.CreateAPIView):
    '''create a new review'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailsApiVeiw(generics.RetrieveUpdateDestroyAPIView):
    '''get | update | delete a specific review'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
