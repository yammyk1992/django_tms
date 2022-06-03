from django.db import models


# Create your models here.
from publication_app.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=128)
    posts = models.ManyToManyField(Post, related_name='tags')
