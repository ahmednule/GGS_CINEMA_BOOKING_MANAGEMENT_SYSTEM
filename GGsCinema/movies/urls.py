from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home_page'),
    path('showing/', views.showing, name='showing_page'),
    path('booking/', views.booking, name='booking_page'),
    path('booking/<int:movie_id>/', views.booking, name='booking_page'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking_page'),
    path('confirm_booking/<int:id>/', views.confirm_booking, name='confirm_booking_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)