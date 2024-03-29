from django.db import models
from django.contrib.auth.models import User


class Messenger(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messenger_sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messenger_recipient')
    text = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
