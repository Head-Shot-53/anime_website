from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from anime_list.models import FavoriteAnime, Anime, Category
from django.db.models import Count, Avg


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # автоматичний вхід після реєстрації
            messages.success(request, 'Реєстрація успішна! Ласкаво просимо!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def user_logout(request):
    print('вихід вдалий')
    logout(request)
    return render(request, 'users/logout.html') 

@login_required
def profile(request):
    favorite_animes = request.user.favorite_anime_list.all()  # Отримуємо улюблені аніме
    return render(request, 'users/profile.html', {'favorite_anime': favorite_animes})

@login_required
def anime_watch_history(request):
    """Зберігає історію перегляду аніме користувача"""
    
    # Отримуємо список останніх переглянутих аніме з сесії
    recent_animes = request.session.get('recent_animes', [])
    
    # Отримуємо аніме з бази даних за списком ID
    watched_animes = Anime.objects.filter(id__in=recent_animes)

    return render(request, 'users/watch_history.html', {
        'watched_animes': watched_animes
    })

def get_recommended_animes(user):
    """Функція для створення списку рекомендованих аніме"""
    
    # Отримуємо улюблені аніме користувача
    favorite_animes = user.favorite_anime_list.all()

    # Отримуємо історію переглядів користувача (якщо є)
    watched_animes = user.watch_history_list.all()

    # Збираємо всі жанри, які цікавлять користувача
    user_categories = Category.objects.filter(animes__in=favorite_animes).distinct()

    # Вибираємо всі аніме, які мають хоча б один жанр, що цікавить користувача
    recommended_animes = Anime.objects.filter(categories__in=user_categories).exclude(id__in=favorite_animes).distinct()

    # Відбираємо тільки популярні аніме (за рейтингом)
    recommended_animes = recommended_animes.annotate(avg_rating=Avg('ratings__score')).filter(avg_rating__gte=7.0)

    # Сортуємо за рейтингом та кількістю переглядів
    recommended_animes = recommended_animes.order_by('-avg_rating')[:10]

    return recommended_animes


@login_required
def recommendations_view(request):
    # Отримуємо список улюблених аніме користувача
    favorite_anime_objects = FavoriteAnime.objects.filter(user=request.user).select_related('anime')

    # Отримуємо список ID улюблених аніме
    favorite_anime_ids = [fav.anime.id for fav in favorite_anime_objects]

    # Отримуємо жанри улюблених аніме
    favorite_categories = Anime.objects.filter(id__in=favorite_anime_ids).values_list('categories', flat=True)

    # Підбираємо рекомендації за жанрами улюблених аніме
    recommended_animes = Anime.objects.filter(categories__in=favorite_categories).exclude(id__in=favorite_anime_ids).distinct()

    return render(request, 'users/recommendations.html', {'recommended_animes': recommended_animes})