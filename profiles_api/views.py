from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


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
