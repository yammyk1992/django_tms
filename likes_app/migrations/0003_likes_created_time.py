# Generated by Django 4.0.6 on 2022-07-06 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('likes_app', '0002_alter_likes_post_alter_likes_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]