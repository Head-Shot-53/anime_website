# Generated by Django 5.1.5 on 2025-01-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_list', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='categories',
            field=models.ManyToManyField(related_name='animes', to='anime_list.category'),
        ),
    ]
