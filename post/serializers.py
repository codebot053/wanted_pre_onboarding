# DRF
from rest_framework import serializers

#local
from .models import Technology, Post


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields=['name']

class PostSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Post
        fields = ['company', 'position', 'job_reward', 'content', 'technologies_needed']