

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from comments_app.models import Comments
from publication_app.models import Post


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_time = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} поставил лайк посту - {self.post.title}"

    # составной индекс для того что бы можно было лайкнуть только один раз один пост
    class Meta:
        unique_together = (('user', 'post'),)


class LikesComments(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="like_comment_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
