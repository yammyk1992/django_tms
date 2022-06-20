from rest_framework import serializers

from ...models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        exclude = ('posts', 'id')


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['posts', 'id']

    posts_count = serializers.SerializerMethodField()

    @staticmethod
    def get_posts_count(self, instance) -> int:
        return instance.posts_count()
