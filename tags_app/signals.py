import re

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Tag
from publication_app.models import Post


@receiver(post_save, sender=Post)
def create_tags(sender, instance, created, *args, **kwargs):
    for tag_name in re.findall(r"#(\w+)", instance.content):
        tag, is_created = Tag.objects.get_or_create(name=tag_name.lower())
        tag.posts.add(instance)
