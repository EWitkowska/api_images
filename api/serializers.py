from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image

class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Image
        fields = "__all__"

class ImagePremiumSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Image
        fields = ('author', 'thumbnail_200', 'thumbnail_400', 'image')
