# Generated by Django 3.0.6 on 2020-05-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200514_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Слаг'),
        ),
    ]