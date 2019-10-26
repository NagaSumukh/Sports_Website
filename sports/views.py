from django.shortcuts import render
from .models import Player,PlayerEng
from .models import Teamranking
from .models import Teamrankingodi
from .models import News
# Create your views here.

def playerinfo(request) :
    players = Player.objects.all()
    return render(request,"playerinfo.html",{'players' : players})

def playerinfoeng(request) :
    players = PlayerEng.objects.all()
    return render(request,"playerinfoeng.html",{'players':players})

def mainhome(request):
    news = News.objects.all()
    return render(request,"mainhome.html",{'news':news})

def teamranking(request):
    teams = Teamranking.objects.all()
    news = News.objects.all()
    return render(request,"ranking.html",{'teams':teams,'news':news})

def teamrankingodi(request):
    #teams = Teamrankingodi.objects.all().order_by('id').reverse()
    teams = Teamrankingodi.objects.all()
    news = News.objects.all()
    return render(request,"rankingodi.html",{'teams':teams,'news':news})

def news1(request):
    return render(request,"news1.html")
def news2(request):
    return render(request,"news2.html")