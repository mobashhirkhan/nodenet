# Generated by Django 4.2.6 on 2023-11-14 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0023_friendrequest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='type',
            field=models.CharField(default='Request', editable=False, max_length=200),
        ),
    ]