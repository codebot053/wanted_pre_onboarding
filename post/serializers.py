# django
from django.contrib.auth import get_user_model

# DRF
from rest_framework import serializers

#local
from .models import Technology, Post


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields=['name']

class PostSerializer(serializers.ModelSerializer):

    technologies_needed = TechnologySerializer(many=True,required=False, read_only=True)
    get_technology = serializers.ListField(required=False)

    # 포스팅 생성(post)
    def create(self, validated_data):
        
        get_technology = validated_data.pop('get_technology',[])
        
        job_post = Post.objects.create(**validated_data)
        job_post.technologies_needed.add(*get_technology)
        job_post.save()
        return job_post

    def validate(self, data):
        user_id = data.get('author').id
        user = get_user_model().objects.get(id=user_id)
        if user.is_enterprise == False:
            raise serializers.ValidationError(
                detail={"error": "기업계정 사용자만 작성할 수 있습니다."},
            )
        return data
        
    class Meta:
        model = Post
        fields = ['author','company', 'position', 'job_reward', 'content', 'technologies_needed','get_technology']