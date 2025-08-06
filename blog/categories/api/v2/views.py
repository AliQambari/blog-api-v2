from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from blog.categories.models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
