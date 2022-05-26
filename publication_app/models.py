from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    nationality = models.TextField(max_length=256, unique=False, blank=False, null=False, verbose_name='Национальность')
    content = models.TextField(blank=True, null=False, verbose_name='Пост')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    # для вывода в режиме shell терминал заголовков объектов из базы данных

    def __str__(self):
        return self.title

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Пост'
        # для множественного числа
        verbose_name_plural = 'Спортсмены'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

#
# class PostImage(models.Model):
#     # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
<<<<<<< HEAD
#     images = models.ImageField(null=True, blank=True, verbose_name='Фото')
=======
#     image = models.ImageField(null=True, blank=True, verbose_name='Фото')
>>>>>>> f1cc4431d0109fc20c497aae3b6fddbc0f2fb4de
#     title = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.post


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Категория'
        # для множественного числа
        verbose_name_plural = 'Категории'
        ordering = ['id']
