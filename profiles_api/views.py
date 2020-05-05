from django.shortcuts import render
from django.http import HttpResponse
from django.dispatch import receiver
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# Create your views here.


class HelloAPIView(APIView):
    """Custom designed api end points"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello'})

    def post(self, request):
        """Create a greeting with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            greeting = f'Hello {name}'
            return Response({'message': greeting})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Vie set for CRUD of feed items"""

    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


def facebook_login(request):
    """Get access token for facebook graph API's"""

    url = 'https://graph.facebook.com/oauth/auth_token'
    data = {
        'client_id': '',
        'client_secret': '',
        'grant_type': 'client_credentials',
        'redirect_uri': 'http://localhost:4200/home'
    }

    res = requests.get(url, data)

    return HttpResponse(res)
