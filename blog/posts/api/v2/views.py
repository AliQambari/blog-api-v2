from rest_framework import viewsets
from blog.posts.models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostSerializer
    #using filter by query params on categories :GET /api/v2/posts/?category=2
    filterset_fields = ['categories']
