# Generated by Django 4.0.5 on 2022-06-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0020_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Слаг'),
        ),
    ]
