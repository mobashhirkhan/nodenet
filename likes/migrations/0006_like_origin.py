# Generated by Django 4.2.6 on 2023-11-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0005_alter_like_object_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='origin',
            field=models.TextField(default='', max_length=255),
        ),
    ]
