from django.contrib import admin
from django.urls import path, include

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v2',
        description="API documentation for Blog Project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Version 1: Old manual views
    path('api/v1/categories/', include('blog.categories.api.v1.urls')),
    path('api/v1/posts/', include('blog.posts.api.v1.urls')),

    # Version 2: DRF-based views
    path('api/v2/categories/', include('blog.categories.api.v2.urls')),
    path('api/v2/posts/', include('blog.posts.api.v2.urls')),

    # Swagger & Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
