from enum import unique

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from comments_app.models import Comments
from publication_app.models import Post


class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    # составной индекс для того что бы можно было лайкнуть только один раз один пост
    class Meta:
        unique_together = (('user', 'post'),)


class LikesComments(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="like_comment_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
