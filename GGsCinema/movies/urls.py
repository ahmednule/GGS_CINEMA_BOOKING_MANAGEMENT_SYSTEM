from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('showing/', views.showing, name='showing_page'),
]