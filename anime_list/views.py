from django.shortcuts import render, get_object_or_404
from .models import Anime, Category

def anime_list(request):
    animes = Anime.objects.all() # Отримування всіх аніме з бази
    categories = Category.objects.all() # отримую всі категорії
    return render(request, 'anime_list/anime_list.html', {'animes':animes, 'categories':categories})
 
def anime_detail(request,anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime_list/anime_detail.html', {'anime':anime})

def anime_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    animes = category.animes.all()
    return render(request, 'anime_list/anime_list.html', {'animes':animes, 'select_category':category})
