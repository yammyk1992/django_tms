from rest_framework import routers

from comments_app.api.views.comments import CommentsViewSet

api_router = routers.DefaultRouter()
api_router.register('comments', CommentsViewSet)
