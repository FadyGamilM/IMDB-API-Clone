from rest_framework.serializers import ModelSerializer
from ....models import Review


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        # we must execulde the content field because when we use the endpoint /content/content_pk/reviews/new we shouldn't add the cotnent id in the body of the request
        exclude = ('content',)
