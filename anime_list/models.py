from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=500) # назва
    description = models.TextField() # опис
    release_year = models.IntegerField() # дата виходу
    rating = models.FloatField() # рейтинг
    image_url = models.URLField(blank=True,null=True) # Посилання на обкладинку

    def __str__(self):
        return self.title # вивід назви у Djsngo admin
    
    