from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def stats_details(request, game_name):
    return render(request, 'user_stats.html', {'game_name': game_name})