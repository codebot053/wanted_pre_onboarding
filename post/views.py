# django
from django.shortcuts import render, get_object_or_404

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

    def put(self, request, pk):
        post = get_object_or_404(Post,id=pk)
        default_company = post.company.pk # 채용공고 인스턴스의 회사 pk값
        default_author = post.author.id
        
        
        request.data['author'] = default_author
        request.data['company'] = default_company
        #요청시에 기존 회사,작성자 pk값을 덮어써서 변경 방지
        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        post = get_object_or_404(Post,id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)