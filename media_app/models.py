from django.contrib.auth import get_user_model
from django.db import models


from django.urls import reverse

User = get_user_model()


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    file = models.ImageField(blank=False, null=False)
    uploaded = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('media', kwargs={'media_file': self.file})
