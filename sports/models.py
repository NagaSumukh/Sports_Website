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


