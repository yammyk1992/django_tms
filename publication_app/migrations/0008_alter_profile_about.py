# Generated by Django 4.0.4 on 2022-05-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0007_alter_profile_about_alter_profile_github_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=4096, null=True, verbose_name='О себе'),
        ),
    ]
