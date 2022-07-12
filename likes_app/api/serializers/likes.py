from rest_framework import serializers

from likes_app.models import Likes, LikesComments


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
        read_only_fields = ['user', ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )


class LikesCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesComments
        fields = "__all__"
        read_only_fields = ["user", ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
