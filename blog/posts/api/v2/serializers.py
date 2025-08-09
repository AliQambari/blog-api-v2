from rest_framework import serializers
from blog.posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  
    class Meta:
        model = Post
        fields = ['id', 'title', 'categories', 'updated_at', 'author']  

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

