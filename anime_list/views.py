from django.shortcuts import render, get_object_or_404
from .models import Anime, Category, Rating
from .forms import SearchForm
from django.core.paginator import Paginator
from django.db.models import Avg

def anime_list(request):
    form = SearchForm(request.GET)
    animes = Anime.objects.all()  # Отримуємо всі аніме
    categories = Category.objects.all()  # Отримуємо всі категорії

    if form.is_valid():
        query = form.cleaned_data['query']
        animes = animes.filter(title__icontains=query)  # Фільтруємо аніме по назві

    paginator = Paginator(animes, 5)  # По 10 аніме на сторінку
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

def anime_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    animes = category.animes.all()
    return render(request, 'anime_list/anime_list.html', {'animes':animes, 'select_category':category})
