# Generated by Django 3.2.15 on 2022-08-18 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220818_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
    ]