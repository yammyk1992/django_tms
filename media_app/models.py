from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    file = models.ImageField(blank=False, null=False)
    uploaded = models.DateTimeField(auto_now_add=True)

