from rest_framework import routers

from user_app.api.views.users import UserViewSet

api_router = routers.DefaultRouter()
api_router.register('users', UserViewSet)

