from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_listings', views.get_listings, name='get_listings'),
]
