from rest_framework.viewsets import ModelViewSet

from comments_app.api.serializers.comments import CommentsSerializer
from comments_app.models import Comments


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
