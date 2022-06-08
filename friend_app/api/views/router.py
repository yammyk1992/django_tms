from rest_framework import routers

from friend_app.api.views.friend import FriendViewSet

api_router = routers.DefaultRouter()
api_router.register('friend', FriendViewSet)
