from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from tags_app.api.serializers.tags import TagSerializer
from ...models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
