from rest_framework import filters
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializer.publications import PostSerializer
from ...models import Post


# CRUD
# GET, POST, PUT, PATCH, DELETE

class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']
