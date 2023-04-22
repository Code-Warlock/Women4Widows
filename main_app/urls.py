from django.urls import path
from .views import index,about,contact,mission, projects,team   

urlpatterns = [
    path('',index, name='main-page'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('mission', mission, name='mission'),
    path('projects', projects, name='projects'),
    path('team', team, name='team'),
]