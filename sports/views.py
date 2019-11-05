from django.shortcuts import render
from .models import Player,PlayerEng,PlayerAus,PlayerSa
from .models import Teamranking,Teamrankingodi,PlayerRankingOdiBat,PlayerRankingTestBat
from .models import News,Schedule,Teams,Feedback
# Create your views here.

def playerinfo(request) :
    players = Player.objects.all().order_by('id')
    return render(request,"playerinfo.html",{'players' : players})

def playerinfoeng(request) :
    players = PlayerEng.objects.all().order_by('id')
    return render(request,"playerinfoeng.html",{'players':players})

def playerinfoaus(request) :
    players = PlayerAus.objects.all().order_by('id')
    return render(request,"playerinfoaus.html",{'players':players})

def playerinfosa(request) :
    players = PlayerSa.objects.all().order_by('id')
    return render(request,"playerinfosa.html",{'players':players})

def mainhome(request):
    news = News.objects.all().order_by('id').reverse()
    schedule = Schedule.objects.all()
    return render(request,"mainhome.html",{'news':news,'schedules':schedule})

def teamranking(request):
    teams = Teamranking.objects.all().order_by('id')
    news = News.objects.all()
    return render(request,"ranking.html",{'teams':teams,'news':news})

def teamrankingodi(request):
    #teams = Teamrankingodi.objects.all().order_by('id').reverse()
    teams = Teamrankingodi.objects.all().order_by('id')
    news = News.objects.all()
    return render(request,"rankingodi.html",{'teams':teams,'news':news})

def player_ranking_odi_bat(request):
    news = News.objects.all()
    players = PlayerRankingOdiBat.objects.all().order_by('id')
    return render(request,"player_ranking_odi_bat.html",{'players':players,'news':news})
def player_ranking_test_bat(request):
    news = News.objects.all()
    players = PlayerRankingTestBat.objects.all().order_by('id')
    return render(request,"player_ranking_test_bat.html",{'players':players,'news':news})

def news1(request):
    news = News.objects.all()
    schedule = Schedule.objects.all()
    print(schedule)
    return render(request,"news1.html",{'news':news,'schedules':schedule})
def news2(request):
    news = News.objects.all()
    schedule = Schedule.objects.all()
    print(schedule)
    return render(request,"news2.html",{'news':news,'schedules':schedule})
def news3(request):
    news = News.objects.all()
    schedule = Schedule.objects.all()
    print(schedule)
    return render(request,"news3.html",{'news':news,'schedules':schedule})

def add_feedback(request):
    news = News.objects.all()
    schedule = Schedule.objects.all()

    email = request.POST.get('email',False)
    phno = request.POST.get('phno',False)
    feedback = request.POST.get('feedback',False)

    feedback_val = Feedback(email = email,feedback = feedback,phno = phno)
    feedback_val.save()
    return render(request,"add_feedback.html",{'news':news,'schedules':schedule})