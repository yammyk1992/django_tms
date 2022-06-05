from rest_framework.viewsets import ModelViewSet

from profile_app.models import Profile
from profile_app.serializers.profile import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
