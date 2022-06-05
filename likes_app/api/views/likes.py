from rest_framework.viewsets import ModelViewSet

from likes_app.api.serializers.likes import LikesSerializer, LikesCommentsSerializer
from likes_app.models import Likes, LikesComments


class LikesViewSet(ModelViewSet):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()


class LikesCommentsViewSet(ModelViewSet):
    serializer_class = LikesCommentsSerializer
    queryset = LikesComments.objects.all()
