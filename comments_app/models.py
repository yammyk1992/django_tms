from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models

from publication_app.models import Post, User


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    text_comments = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comments")

    class Meta:
        ordering = ['created_at']
