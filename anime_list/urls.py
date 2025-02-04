from django.urls import path
from .views import anime_list, anime_detail, anime_by_category, category_detail

urlpatterns = [
    path('', anime_list, name='anime_list'),
    path('<int:anime_id>/', anime_detail, name='anime_detail'),
    path('category/<int:category_id>/',anime_by_category,name='anime_by_category'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]