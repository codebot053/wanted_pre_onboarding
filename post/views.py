# django
from django.shortcuts import render

# DRF
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# local
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self,request):
        return Response(PostSerializer(Post.objects.all(), many=True).data, status=status.HTTP_200_OK)
    def post(self, request):
       
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailApiView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def get(self, request, pk):
        return Response(PostSerializer(Post.objects.get(id=pk)).data, status=status.HTTP_200_OK)