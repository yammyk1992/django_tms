# Generated by Django 4.0.5 on 2022-07-01 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0022_alter_imagepost_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]