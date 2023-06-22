from rest_framework.serializers import ModelSerializer
from ....models import StreamingPlatform
class StreamingPlatformSerializer(ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

