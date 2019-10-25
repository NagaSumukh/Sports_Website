from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.mainhome,name='mainhome'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('playerinfo',views.playerinfo,name='playerinfo'),
    path('ranking',views.teamranking,name='ranking')
]

admin.site.site_header = 'Sports Admin'
admin.site.site_title = "Sports Site Admin"
admin.site.index_title = 'Welcome to Admin Page'
