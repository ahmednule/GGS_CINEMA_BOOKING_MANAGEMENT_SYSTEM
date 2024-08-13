from django.contrib import admin
from .models import Movie, Theater, Booking

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Booking)
