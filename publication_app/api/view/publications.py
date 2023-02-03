from rest_framework import filters
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

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

    # включаем поиск и сортировку в API
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'id']
    search_fields = ['=id', 'title', 'content', 'category_id', '^user__username']
