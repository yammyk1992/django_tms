from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from comments_app.models import Comments
from publication_app.models import Post


class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LikesComments(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="like_comment_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
