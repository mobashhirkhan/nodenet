# Generated by Django 4.2.6 on 2023-11-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0004_like_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='object_type',
            field=models.CharField(default='post', max_length=255),
        ),
    ]
