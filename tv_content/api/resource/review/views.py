from rest_framework import mixins
from rest_framework import generics

from .serializer import ReviewSerializer
from ....models import Review


class ReviewListApiView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ReviewCreateApiView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
