from django.contrib import admin
from .models import Player
from .models import Teamranking
from .models import Teams,Schedule, Teamrankingodi
# Register your models here.

admin.site.register(Player)
admin.site.register(Teamranking)
admin.site.register(Teams)
admin.site.register(Schedule)
admin.site.register(Teamrankingodi)
