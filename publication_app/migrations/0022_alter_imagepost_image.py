# Generated by Django 4.0.5 on 2022-06-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0021_remove_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]
