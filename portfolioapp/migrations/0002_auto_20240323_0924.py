# Generated by Django 3.2.24 on 2024-03-23 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='function',
            name='is_main_function',
        ),
        migrations.RemoveField(
            model_name='quality',
            name='social_link',
        ),
        migrations.AddField(
            model_name='owner',
            name='is_main_function',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='is_func_set', to='portfolioapp.function', verbose_name='Is main function'),
        ),
        migrations.AddField(
            model_name='quality',
            name='type_quality',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='type_quality_owner_set', to='portfolioapp.typequality', verbose_name='Type Quality'),
        ),
    ]
