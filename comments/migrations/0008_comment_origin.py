# Generated by Django 4.2.6 on 2023-11-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_alter_comment_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='origin',
            field=models.TextField(default='', max_length=255),
        ),
    ]
