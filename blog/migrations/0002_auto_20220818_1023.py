# Generated by Django 3.2.15 on 2022-08-18 04:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
        migrations.RemoveIndex(
            model_name='blogpost',
            name='blog_post_title_a64c75_idx',
        ),
        migrations.AddIndex(
            model_name='blogpost',
            index=models.Index(fields=['title', 'author', 'category'], name='blog_blogpo_title_c9cb79_idx'),
        ),
    ]
