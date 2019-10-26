from django.shortcuts import render
from .models import Player,PlayerEng,PlayerAus,PlayerSa
from .models import Teamranking
from .models import Teamrankingodi
from .models import News,Schedule,Teams
# Create your views here.

def playerinfo(request) :
    players = Player.objects.all()
    return render(request,"playerinfo.html",{'players' : players})

def playerinfoeng(request) :
    players = PlayerEng.objects.all()
    return render(request,"playerinfoeng.html",{'players':players})

def playerinfoaus(request) :
    players = PlayerAus.objects.all()
    return render(request,"playerinfoaus.html",{'players':players})

def playerinfosa(request) :
    players = PlayerSa.objects.all()
    return render(request,"playerinfosa.html",{'players':players})

def mainhome(request):
    news = News.objects.all()
    schedule = Schedule.objects.get(id=1)
    team1 = schedule.team1_id
    team2 = schedule.team2_id
    firsteam = Teams.objects.get(id=team1)
    secteam = Teams.objects.get(id=team2)
    time = schedule.time
    date = schedule.date
    info = schedule.info
    first_team_name = firsteam.team
    sec_team_name = secteam.team
    first_team_icon = firsteam.teamicon
    sec_team_icon = secteam.teamicon

    return render(request,"mainhome.html",{'news':news,'time':time,'date':date,'info':info,'first_team_name':first_team_name,'sec_team_name':sec_team_name,'first_team_icon':first_team_icon,'sec_team_icon':sec_team_icon})

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