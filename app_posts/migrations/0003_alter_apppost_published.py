# Generated by Django 4.2.6 on 2023-10-26 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0002_alter_apppost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 3, 29, 13, 431433, tzinfo=datetime.timezone.utc)),
        ),
    ]
