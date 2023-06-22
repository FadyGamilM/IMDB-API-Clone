from rest_framework.serializers import ModelSerializer
from ....models import StreamingPlatform
from ....api.resource.content.serializer import ContentSerializer
class StreamingPlatformSerializer(ModelSerializer):
    # to show the contents that this streaming platform streams when we view each platform 
    streamed_content = ContentSerializer(many=True, read_only = True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

