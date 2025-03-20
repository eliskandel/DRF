from rest_framework import serializers
from ..models import WatchList, Platform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(many=True)
    class Meta:
            model=Review
            exclude=('watchlist', )   
class WatchListSerializer(serializers.ModelSerializer):
    
    reviews=ReviewSerializer(many=True, read_only=True)
    class Meta:
        model=WatchList
        fields='__all__'

class PlatformSerializer(serializers.ModelSerializer):
    # watchlist=WatchListSerializer(many=True, read_only=True)
    watchlist=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Platform
        fields='__all__'


        # exclude=['active']
        # fields=['id','name', 'description']\
    
    # def get_length(self, object):
    #     return len(object.name)
    
    # def validate(self,data):
    #     if data.get("name") == data.get("description"):
    #         raise serializers.ValidationError("Name and description cant be same")
    #     return data

    
    # def validate_data(value):
    #     if len(value) <2:
    #         raise serializers.ValidationError("Name too Short")
    #     return value

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description= serializers.CharField()
#     active=serializers.BooleanField()  

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description', instance.description)
#         instance.active=validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self,data):
#         if data.get("name") == data.get("description"):
#             raise serializers.ValidationError("Name and description cant be same")
#         return data

    
#     def validate_data(value):
#         if len(value) <2:
#             raise serializers.ValidationError("Name too Short")
#         return value