# Generated by Django 4.0.4 on 2022-06-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publication_app', '0016_remove_post_tags_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('posts', models.ManyToManyField(related_name='tags', to='publication_app.post')),
            ],
        ),
    ]
