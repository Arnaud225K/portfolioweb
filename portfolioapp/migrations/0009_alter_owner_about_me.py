# Generated by Django 3.2.24 on 2024-04-13 08:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_function_sociallink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='about_me',
            field=tinymce.models.HTMLField(verbose_name='About me'),
        ),
    ]
