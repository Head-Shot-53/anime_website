from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime, Category, Rating, FavoriteAnime
from .forms import SearchForm
from django.core.paginator import Paginator
from django.db.models import Avg
from django.http import JsonResponse

def anime_list(request):
    form = SearchForm(request.GET)
    animes = Anime.objects.all()  # Отримуємо всі аніме
    categories = Category.objects.all()  # Отримуємо всі категорії

    if form.is_valid():
        query = form.cleaned_data['query']
        animes = animes.filter(title__icontains=query)  # Фільтруємо аніме по назві

    paginator = Paginator(animes, 8)  # По 8 аніме на сторінку
    page_number = request.GET.get('page')  # Отримуємо номер сторінки з GET параметрів
    animes_page = paginator.get_page(page_number)  # Отримуємо сторінку аніме

    return render(request, 'anime_list/anime_list.html', {'animes': animes_page, 'categories': categories, 'form': form})
 
def anime_detail(request, anime_id):
    # Отримуємо об'єкт аніме за його ID
    anime = get_object_or_404(Anime, id=anime_id)
    
    # Обробка POST запиту для оцінки
    if request.method == 'POST':
        score = request.POST.get('score')
        
        if score:
            # Перевіряємо, чи вже є оцінка цього користувача для цього аніме
            rating, created = Rating.objects.get_or_create(
                anime=anime,
                user=request.user,
                defaults={'score': score}
            )
            
            # Якщо оцінка вже існує, оновлюємо її
            if not created:
                rating.score = score
                rating.save()
    
    # Обчислюємо середній рейтинг аніме
    average_rating = anime.ratings.all().aggregate(Avg('score'))['score__avg']
    
    # Повертаємо шаблон з передачею аніме і середнього рейтингу
    return render(request, 'anime_list/anime_detail.html', {'anime': anime,'average_rating': average_rating})

# def anime_by_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     animes = category.animes.all()
#     return render(request, 'base.html', {'animes':animes, 'category':category})


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    # Фільтрація аніме за категорією
    animes = Anime.objects.filter(categories=category)

    return render(request, 'anime_list/category_detail.html', {
        'category': category,
        'animes': animes,
        'categories': Category.objects.all()
    })

# додавання аніме в улюблене
def toggle_favorite(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    favorite, created = FavoriteAnime.objects.get_or_create(user=request.user, anime = anime)

    if not created:
        favorite.delete() # видаляє аніме, якщо воно вже було додано
    return redirect('anime_detail', anime_id = anime.id)


def favorite_anime(request):
    favorite_animes = Anime.objects.filter(favoriteanime__user=request.user)
    return render(request, 'anime_list/favorite_anime.html', {'favorite_animes': favorite_animes})


def remove_favorite(request, anime_id):
    anime = get_object_or_404(FavoriteAnime, user=request.user, anime_id=anime_id)
    anime.delete()
    return redirect('favorite_anime')

def popular_anime(request):
    animes = Anime.objects.order_by('-rating')[:10]  # Топ-10 аніме
    return render(request, 'anime_list/popular.html', {'animes': animes})

def search_anime(request):
    query = request.GET.get('q', '')
    results = Anime.objects.filter(title__icontains=query)[:5]  # Пошук по назві (до 5 результатів)
    
    data = [{"id": anime.id, "title": anime.title} for anime in results]
    
    return JsonResponse(data, safe=False)  # Повертаємо JSON