# Generated by Django 4.2.6 on 2023-11-15 06:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0025_alter_friendrequest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='they_follow_me', to=settings.AUTH_USER_MODEL),
        ),
    ]
