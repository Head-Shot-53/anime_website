from django.shortcuts import render, get_object_or_404
from .models import Anime

def anime_list(request):
    animes = Anime.objects.all() # Отримування всіх аніме з бази
    return render(request, 'anime_list/anime_list.html', {'animes':animes})
 
def anime_detail(request,anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime_list/anime_detail.html', {'anime':anime})

