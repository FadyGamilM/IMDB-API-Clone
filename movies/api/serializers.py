from rest_framework import serializers
from ..models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    is_published = serializers.BooleanField()

    def create(self, validated_data):
        """
            validated_data -> are the dictionary which contains all the elements of the Movie class
            once we get this validated data, we will create an instance in the database
        """
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.save()
        return instance