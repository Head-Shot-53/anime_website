# Generated by Django 5.1.5 on 2025-02-17 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_list', '0007_favoriteanime'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteanime',
            name='added_at',
        ),
        migrations.AlterField(
            model_name='favoriteanime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_anime_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched_at', models.DateTimeField(auto_now_add=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_list.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_history_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-watched_at'],
            },
        ),
    ]
