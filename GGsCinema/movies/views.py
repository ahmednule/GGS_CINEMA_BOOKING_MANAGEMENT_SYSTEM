from django.shortcuts import render, get_object_or_404
from .models import Movie, Theater

def home(request):
    return render(request, 'movies/index.html')

def showing(request):
    # Get all movies from the database
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/showing.html', context)

def booking(request, movie_id):
    # Get the movie with the given ID
    movie = get_object_or_404(Movie, id=movie_id)
    theaters = Theater.objects.all()  # Assuming you want to list all available theaters
    context = {
        'movie': movie,
        'theaters': theaters
    }
    return render(request, 'movies/booking.html', context)

def confirm_booking(request, movie_id):
    # Get the movie with the given ID
    movie = get_object_or_404(Movie, id=movie_id)
    selected_date = request.POST.get('date')
    selected_theater = request.POST.get('theater')
    selected_time = request.POST.get('time')
    
    context = {
        'movie': movie,
        'selected_date': selected_date,
        'selected_theater': selected_theater,
        'selected_time': selected_time,
    }
    return render(request, 'movies/confirm_booking.html', context)
