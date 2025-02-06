from django.urls import path
from .views import anime_list, anime_detail, category_detail, toggle_favorite, favorite_anime, remove_favorite

urlpatterns = [
    path('', anime_list, name='anime_list'),
    path('<int:anime_id>/', anime_detail, name='anime_detail'),
    # path('category/<int:category_id>/',anime_by_category,name='anime_by_category'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('favorite/<int:anime_id>/', toggle_favorite, name = 'toggle_favorite'),
    path('favorites/', favorite_anime, name='favorite_anime'),
    path('favorites/remove/<int:anime_id>/', remove_favorite, name='remove_favorite'),

]