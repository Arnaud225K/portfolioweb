# Generated by Django 3.2.24 on 2024-05-12 11:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Description'),
        ),
    ]
