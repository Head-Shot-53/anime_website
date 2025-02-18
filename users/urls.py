from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, user_logout, anime_watch_history, recommendations_view

urlpatterns = [
    path('register/', register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('profile/',profile,name='profile'),
    path('logout/', user_logout, name='logout'),
    path('watch-history/', anime_watch_history, name='watch_history'),
    path('recommendations/', recommendations_view, name='recommendations'),
]