from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.all()
    return render(request, 'movies/index.html', {
        'latest_movie_list': latest_movie_list
    })

def add_movie(request):
    return render(request, 'movies/Agregar_pelicula.html')


def upload_movie(request):

    return redirect(request, 'movies/index.html') 