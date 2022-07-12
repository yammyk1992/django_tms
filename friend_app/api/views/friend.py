from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.friend import FriendSerializer, FollowSerializer
from ...models import Friend, FollowRequest


class FriendViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class FollowViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = FollowRequest.objects.all()
