from django.shortcuts import render
from .models import Player
# Create your views here.

def playerinfo(request) :



    players = Player.objects.all()

    return render(request,"playerinfo.html",{'players' : players})