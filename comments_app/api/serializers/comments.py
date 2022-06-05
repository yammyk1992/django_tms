from rest_framework import serializers

from likes_app.models import LikesComments
from ...models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('created_at', 'author')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )


# TODO: "доделать "
class LikeCommentsSerializer(serializers.ModelSerializer):
    # user = ProfileSerializer(read_only=True)

    class Meta:
        model = LikesComments
        fields = "user",
