from django.contrib import admin
from .models import Anime, Category

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating')  # Поля, які будуть відображатися в списку
    filter_horizontal = ('categories',)  # Додає зручний віджет для вибору кількох жанрів

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Category)
