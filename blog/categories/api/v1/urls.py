from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>/', views.category_router, name='category_router'),
]