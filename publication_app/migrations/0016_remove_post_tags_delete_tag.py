# Generated by Django 4.0.4 on 2022-06-03 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0015_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
