from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.tag}'
