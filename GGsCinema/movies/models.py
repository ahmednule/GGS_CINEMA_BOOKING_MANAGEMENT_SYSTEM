from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    director = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return self.title

class Theater(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.movie.title} at {self.theater.name} on {self.date} at {self.time}'
