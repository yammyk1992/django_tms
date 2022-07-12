# Generated by Django 4.0.6 on 2022-07-12 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend_app', '0005_remove_friend_users_friend_users_receivers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='friendship_result',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friendship_request', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='user_invite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friendship', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('user', 'user_invite')},
        ),
        migrations.RemoveField(
            model_name='friend',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='users_receivers',
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_request', to=settings.AUTH_USER_MODEL)),
                ('user_follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'user_follow')},
            },
        ),
    ]
