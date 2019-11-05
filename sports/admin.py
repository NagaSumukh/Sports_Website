from django.contrib import admin
from .models import Player,PlayerEng,PlayerAus,PlayerSa
from .models import Teamranking
from .models import Teams,Schedule, Teamrankingodi,News,Feedback
from .models import PlayerRankingOdiBat,PlayerRankingTestBat
# Register your models here.

admin.site.register(Player)
admin.site.register(Teamranking)
admin.site.register(Teams)
admin.site.register(Schedule)
admin.site.register(Teamrankingodi)
admin.site.register(News)
admin.site.register(PlayerEng)
admin.site.register(PlayerAus)
admin.site.register(PlayerSa)
admin.site.register(Feedback)
admin.site.register(PlayerRankingOdiBat)
admin.site.register(PlayerRankingTestBat)