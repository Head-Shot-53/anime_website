from django.db import models
from django.contrib.auth.models import User

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
    number_of_series = models.IntegerField(default=0) # к-ть серій

    def __str__(self):
        return self.title # вивід назви у Djsngo admin
    
class Rating(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=1)

    class Meta:
        unique_together = ('anime', 'user')

    def __str__(self):
        return f"{self.user.username} rated {self.anime.title} with {self.score}"
    
class FavoriteAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_anime_list")  # Унікальний related_name
    anime = models.ForeignKey("Anime", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'anime')  # Користувач не може додати одне аніме кілька разів

    def __str__(self):
        return f"{self.user.username} - {self.anime.title}"

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch_history_list")  # Унікальний related_name
    anime = models.ForeignKey("Anime", on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-watched_at']

    def __str__(self):
        return f"{self.user.username} переглянув {self.anime.title}"