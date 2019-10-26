from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.mainhome,name='mainhome'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('playerinfo',views.playerinfo,name='playerinfo'),
    path('playerinfoeng',views.playerinfoeng,name='playerinfoeng'),
    path('ranking',views.teamranking,name='ranking'),
    path('rankingodi',views.teamrankingodi,name='rankingodi'),
    path('news1',views.news1,name='news1'),
    path('news2',views.news2,name='news2')
]

admin.site.site_header = 'Sports Admin'
admin.site.site_title = "Sports Site Admin"
admin.site.index_title = 'Welcome to Admin Page'
