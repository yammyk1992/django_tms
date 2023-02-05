from rest_framework.viewsets import ModelViewSet

from likes_app.api.serializers.likes import LikesSerializer, LikesCommentsSerializer
from likes_app.models import PostLikes, LikesComments


class LikesViewSet(ModelViewSet):
    serializer_class = LikesSerializer
    queryset = PostLikes.objects.all()


class LikesCommentsViewSet(ModelViewSet):
    serializer_class = LikesCommentsSerializer
    queryset = LikesComments.objects.all()
