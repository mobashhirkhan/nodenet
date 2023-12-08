# Generated by Django 4.2.6 on 2023-10-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0013_alter_apppost_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='contentType',
            field=models.CharField(choices=[('plain', 'plain'), ('markdown', 'markdown'), ('hyperlink', 'hyperlink'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default=('plain', 'plain'), max_length=20),
        ),
    ]
