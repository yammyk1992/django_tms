from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models

from publication_app.models import Post, User


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text_comments = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ['created_at']
