from rest_framework.serializers import ModelSerializer
from ..models import Content, StreamingPlatform

class ContentSerializer (ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class StreamingPlatformSerializer(ModelSerializer):

    class Meta:
        model = StreamingPlatform
        fields = '__all__'

