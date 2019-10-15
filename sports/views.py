from django.shortcuts import render
from .models import Player
from .models import Teamranking
# Create your views here.

def playerinfo(request) :
    players = Player.objects.all()

    return render(request,"playerinfo.html",{'players' : players})

def mainhome(request):
    return render(request,"mainhome.html")

def teamranking(request):
    teams = Teamranking.objects.all()
    return render(request,"teamranking.html",{'teams':teams})