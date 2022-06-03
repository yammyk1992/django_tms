from pyexpat import model

from rest_framework import serializers

from ...models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
