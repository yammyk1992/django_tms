from rest_framework import routers

from .friend import FriendViewSet, FollowViewSet

api_router = routers.DefaultRouter()
api_router.register('friend', FriendViewSet)
api_router.register('follow', FollowViewSet)
