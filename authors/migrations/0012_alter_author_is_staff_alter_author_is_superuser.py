# Generated by Django 4.2.6 on 2023-10-28 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0011_alter_author_displayname_alter_author_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
