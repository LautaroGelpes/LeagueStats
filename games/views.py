from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def game_list(request):
    return render(request, 'games/game_screen.html')
    #Ya toma la carpeta de templates