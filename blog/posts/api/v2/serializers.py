from rest_framework import serializers
from blog.posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'categories', 'updated_at']
        read_only_fields = ['id', 'updated_at']
