from rest_framework.viewsets import ModelViewSet

from profile_app.api.serializers.profile import ProfileSerializer
from profile_app.models import Profile


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
