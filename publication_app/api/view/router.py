from rest_framework import routers

from .publications import PostsViewSet

api_router = routers.DefaultRouter()
api_router.register('posts', PostsViewSet)
