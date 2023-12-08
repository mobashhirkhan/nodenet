# Generated by Django 4.2.6 on 2023-11-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0025_alter_apppost_comment_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='comment_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='apppost',
            name='contentMarkdown',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='apppost',
            name='contentPlain',
            field=models.TextField(default='', editable=False),
        ),
    ]