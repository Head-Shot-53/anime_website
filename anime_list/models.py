from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=500) # назва
    description = models.TextField() # опис
    release_year = models.IntegerField() # дата виходу
    rating = models.FloatField() # рейтинг
    categories = models.ManyToManyField(Category, related_name='animes')
    image = models.ImageField(upload_to='anime_images/', blank = True, null = True) # поле для зображення 

    def __str__(self):
        return self.title # вивід назви у Djsngo admin
    
