# Generated by Django 5.1.5 on 2025-01-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_list', '0003_anime_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='image_url',
        ),
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='anime_images/'),
        ),
    ]
