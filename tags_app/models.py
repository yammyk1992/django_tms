from django.db import models
from django.urls import reverse


class Tag(models.Model):
    tag = models.CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_id': self.pk})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
