from rest_framework.serializers import ModelSerializer
from ....models import StreamingPlatform
from ....api.resource.content.serializer import ContentSerializer


class StreamingPlatformSerializer(ModelSerializer):
    # to show the contents that this streaming platform streams when we view each platform
    # you have to use the same name that i used in the models as a related_name field
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = StreamingPlatform
        exclude = ('content')
