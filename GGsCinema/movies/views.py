from django.shortcuts import render


def home(request):
    return render(request, 'movies/index.html')

def showing(request):
    return render(request, 'movies/showing.html')