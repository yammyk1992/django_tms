from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import include, path

from profile_app import views
from profile_app.api.views.profile import ProfileViewSet
# from profile_app.views import show_profile
from profile_app.views import ProfileEdit

urlpatterns = [
    path('api/profile', ProfileViewSet.as_view({"get": "list", "post": "create"}), name='api_profile'),
    # path('profile/', show_profile, name='profile'),
    path('profile/', login_required(ProfileEdit.as_view()), name='profile_account'),
    ]
