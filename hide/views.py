from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from .models import HiddenMovie

def index(request):
    hidden_movies = HiddenMovie.objects.filter(user=request.user).select_related('movie') if request.user.is_authenticated else []
    return render(request, 'hide/index.html', {'hidden_movies': hidden_movies})

@login_required
def hide_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    HiddenMovie.objects.get_or_create(user=request.user, movie=movie)
    return redirect('movies.index')

@login_required
def unhide_movie(request, movie_id):
    HiddenMovie.objects.filter(user=request.user, movie_id=movie_id).delete()
    return redirect('hide.index')
