from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

from .models import Movie
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)

