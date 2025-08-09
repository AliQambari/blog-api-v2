from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from blog.posts.models import Post
from .serializers import PostSerializer
from blog.core.auth import IsOwnerOrReadOnly  

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['categories']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(
        operation_summary="List Posts",
        operation_description="Retrieve a list of all posts",
        tags=['Posts']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create Post",
        operation_description="Create a new post associated with the authenticated user",
        tags=['Posts']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve Post",
        operation_description="Retrieve details of a specific post by ID",
        tags=['Posts']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Post",
        operation_description="Update all fields of a specific post owned by the authenticated user",
        tags=['Posts']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial Update Post",
        operation_description="Update one or more fields of a specific post owned by the authenticated user",
        tags=['Posts']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Post",
        operation_description="Delete a specific post owned by the authenticated user by ID",
        tags=['Posts']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
