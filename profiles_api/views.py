from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class HelloAPIView(APIView):
    """Custom designed api end points"""

    def get(self, request, format=None):
        return Response({'message': 'Hello'})
