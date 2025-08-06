from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('<int:post_id>/', views.post_router, name='post_router'),
    path('category/<int:category_id>/', views.get_posts_by_category, name='posts_by_category'),
    #EXAMPLE: /api/v1/posts/category/2/ 
]