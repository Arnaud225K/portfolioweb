# Generated by Django 3.2.24 on 2024-04-21 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_skill_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='color',
        ),
    ]
