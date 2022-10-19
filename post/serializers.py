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
    def update(self, instance, validated_data):
        # m2m으로 관계된 필드 technologies_needed 의 업데이트처리를 위해 부모클래스의 update를 상속받아 처리했습니다.
        # 기존 값을 초기화 하고 다시 입력 받은 값을 등록합니다. 
        if ('get_technology' in validated_data):
            get_technology = validated_data.pop('get_technology',[])
            instance.technologies_needed.set([])
            instance.technologies_needed.add(*get_technology)
            instance.save()
        return super().update(instance, validated_data)
    
    class Meta:
        model = Post
        fields = ['id','author','company', 'position', 'job_reward', 'content', 'technologies_needed','get_technology']