from rest_framework.serializers import ModelSerializer
from ....models import Review
from rest_framework import serializers


class ReviewSerializer(ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # we must execulde the content field because when we use the endpoint /content/content_pk/reviews/new
        # we shouldn't add the cotnent id in the body of the request
        exclude = ('content',)
