from django.urls import include, path

from comments_app.api.views.router import api_router
from profile_app.api.views.profile import ProfileViewSet

urlpatterns = [
    path('api/profile', ProfileViewSet.as_view({"get": "list", "post": "create"}), name='api_profile'),
]
