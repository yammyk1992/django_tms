from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from friend_app.api.serializers.friend import FriendSerializer
from friend_app.models import Friend


class FriendViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
