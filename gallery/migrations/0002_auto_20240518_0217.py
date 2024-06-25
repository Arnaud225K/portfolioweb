# Generated by Django 3.2.24 on 2024-05-18 02:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/image', verbose_name='Main image'),
        ),
    ]
