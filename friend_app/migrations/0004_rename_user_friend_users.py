# Generated by Django 4.0.4 on 2022-06-12 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend_app', '0003_rename_users_friend_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='user',
            new_name='users',
        ),
    ]
