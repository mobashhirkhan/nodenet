# Generated by Django 4.2.6 on 2023-12-04 22:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0033_author_foreign_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='id2',
            field=models.TextField(default=uuid.uuid4, editable=False),
        ),
    ]
