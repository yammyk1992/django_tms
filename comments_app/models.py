from django.contrib.auth import get_user_model
from django.db import models

from publication_app.models import Post

User = get_user_model()


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text_comments = models.CharField(max_length=256, blank=False, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.text_comments}'

    class Meta:
        ordering = ['created_at']
