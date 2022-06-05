# Generated by Django 4.0.4 on 2022-05-27 22:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(max_length=4096, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9, 15}$')], verbose_name='Номер телефона'),
        ),
    ]