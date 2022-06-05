from rest_framework import routers

from likes_app.api.views.likes import LikesViewSet, LikesCommentsViewSet

api_router = routers.DefaultRouter()
api_router.register("like", LikesViewSet)
api_router.register("like_comments", LikesCommentsViewSet)
