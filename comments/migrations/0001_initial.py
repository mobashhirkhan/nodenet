# Generated by Django 4.2.6 on 2023-10-26 03:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('liked', models.ManyToManyField(to='likes.like')),
            ],
        ),
    ]
