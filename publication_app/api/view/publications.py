from rest_framework import filters
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ..serializer.publications import PostSerializer
from ...models import Post


# CRUD
# GET, POST, PUT, PATCH, DELETE

class PostsViewSet(ModelViewSet):
    # GenericViewSet,
    # ListModelMixin,
    # CreateModelMixin,
    # DestroyModelMixin,
    # UpdateModelMixin,
    # RetrieveModelMixin

    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']
