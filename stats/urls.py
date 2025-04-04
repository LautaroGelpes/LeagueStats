from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_home, name='stats_home'),
]