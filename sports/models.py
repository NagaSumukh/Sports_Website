from django.db import models

# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    battingstyle  = models.CharField(max_length=150)
    bowlingstyle = models.CharField(max_length=150)
    iccrank = models.IntegerField()
    matches = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()

class PlayerEng (models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    battingstyle  = models.CharField(max_length=150)
    bowlingstyle = models.CharField(max_length=150)
    iccrank = models.IntegerField()
    matches = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()

class Teamranking (models.Model) :
    position = models.IntegerField()
    team = models.CharField(max_length=150)
    rating = models.IntegerField()
    points = models.IntegerField()

class Teamrankingodi (models.Model):
    position = models.IntegerField()
    team = models.CharField(max_length=150)
    rating = models.IntegerField()
    points = models.IntegerField()

class Teams (models.Model) :
    team = models.CharField(max_length=150)
    teamicon = models.ImageField(upload_to='pics')
    def __str__(self) :
        return "%s" %(self.team)

class Schedule(models.Model):
    team1 = models.ForeignKey(Teams,related_name='team1',on_delete=models.CASCADE)
    team2 = models.ForeignKey(Teams,related_name='team2',on_delete=models.CASCADE)
    date = models.CharField(max_length=250)
    time = models.CharField(max_length=150)
    info = models.CharField(max_length=300)

class News(models.Model):
    url = models.URLField(max_length=1000)
    head = models.CharField(max_length=500)
    info = models.CharField(max_length=500)


