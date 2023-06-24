from rest_framework.serializers import ModelSerializer
from ....models import Content
from ..review.serializer import ReviewSerializer


class ContentSerializer (ModelSerializer):
    # read only is true because we need this field to be accessed on get requests only but in post requests we won't enter this field
    # notice that the name of the field must be the same as we mentioned in the `related_field` in the model of the Review 
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        exclude = ('streaming_platform',)
