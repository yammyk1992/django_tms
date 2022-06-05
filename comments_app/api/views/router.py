from rest_framework import routers

from .comments import CommentsViewSet

api_router = routers.DefaultRouter()
api_router.register('comments', CommentsViewSet)
