from django.shortcuts import render
from rest_framework import viewsets
from .models import Image, Profile
from rest_framework import permissions
from .serializers import UserSerializer, ImageSerializer, ImagePremiumSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    def get_user(self):

        user = self.request.user
        return user
    
    def get_serializer_class(self):
       
        user = self.get_user()
        user_account = self.queryset.values_list('account_type').filter(id=user.id)
        if user_account == 'BASIC':
            return ImageSerializer
        if user_account == 'PREMIUM':
            return ImagePremiumSerializer

class ImageViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_user(self):

        user = UserViewSet.get_user(self)
        return user
        
    def get_queryset(self):

        user = self.get_user()
        return Image.objects.filter(author=user)
