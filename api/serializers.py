from rest_framework import serializers

from .models import FunctionTurnPointModel, StatusModel, ImageModel

class PhotoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionTurnPointModel
        fields = '__all__'

class StatuisPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'