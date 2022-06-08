from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from friend_app.api.serializers.friend import FriendSerializer
from friend_app.models import Friend


class FriendViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
