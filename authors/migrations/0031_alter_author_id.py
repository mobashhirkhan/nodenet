# Generated by Django 4.2.6 on 2023-11-24 21:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0030_friendrequest_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
