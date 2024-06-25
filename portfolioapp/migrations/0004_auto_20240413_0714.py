# Generated by Django 3.2.24 on 2024-04-13 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_auto_20240406_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='language_owner',
        ),
        migrations.AddField(
            model_name='language',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='owner_language_set', to='portfolioapp.owner'),
        ),
    ]