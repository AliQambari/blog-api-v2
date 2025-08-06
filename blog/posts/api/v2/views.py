from rest_framework import viewsets
from blog.posts.models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostSerializer
