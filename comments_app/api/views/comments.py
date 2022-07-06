from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comments import CommentsSerializer
from comments_app.models import Comments


class CommentsViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    filter_backends = [filters.OrderingFilter]
