from rest_framework import serializers
from ..models import Movie


################################### Default Serializer ############################################
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     is_published = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#             validated_data -> are the dictionary which contains all the elements of the Movie class
#             once we get this validated data, we will create an instance in the database
#         """
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.save()
#         return instance
#####################################################################################################


################################### Model Serializer ############################################
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # we define if we need to execlude specific fields or speicfy the fields we need to include any one of them is 
        fields = ['id', 'name', 'description_length'] # or : exclude = ['description', 'is_published']

    # we can also define custom fields that are not defined before in the model by defining these fields as 
    # serializer model fields as following : 
    description_length = serializers.SerializerMethodField() # now we need to calculate this field via a get method as following : 

    # get_[the field] is the naming convention 
    def get_description_length(self, object:Movie): # object has an access to all fields 
        return len(object.description)

#####################################################################################################
