from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.mainhome,name='mainhome'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('playerinfo',views.playerinfo,name='playerinfo'),
    path('playerinfoeng',views.playerinfoeng,name='playerinfoeng'),
    path('playerinfoaus',views.playerinfoaus,name='playerinfoaus'),
    path('playerinfosa',views.playerinfosa,name='playerinfosa'),
    path('ranking',views.teamranking,name='ranking'),
    path('rankingodi',views.teamrankingodi,name='rankingodi'),
    path('news1',views.news1,name='news1'),
    path('news2',views.news2,name='news2'),
    path('news3',views.news3,name='news3'),
    path('add_feedback',views.add_feedback,name='add_feedback')
]

admin.site.site_header = 'Sports Admin'
admin.site.site_title = "Sports Site Admin"
admin.site.index_title = 'Welcome to Admin Page'
