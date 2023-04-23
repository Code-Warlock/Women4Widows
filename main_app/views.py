from django.shortcuts import redirect, render

# Create your views here.
from random import choice
from .permanent_data import data,widows_url
two_urls = []
while len(two_urls) <= 2:
    two_urls.append(choice(widows_url))
def index(request):
    context = {
        "url1" : two_urls[0] + ".jpg",
        "url2" : two_urls[1] + ".jpg",
        "title" : "Home",
        "name_main": data['name_main'],
        "name_secondary": data['name_secondary'],
        "goals": data['goals'],
    }
    return render(request, 'main_app/index.html', context)

def about(request):
    context = {
        "title" : "About Us"
    }
    return render(request, 'main_app/about.html',context)

def contact(request):
    context = {
        "title" : "Contact"
    }
    return render(request, 'main_app/contact.html',context)

def mission(request):
    context = {
        "title" : "Mission"
    }
    return render(request, 'main_app/mission.html',context)

def team(request):
    context = {
        "title" : "Team"
    }
    return render(request, 'main_app/team.html',context)

def projects(request):
    context = {
        "projects" : "projects"
    }
    return render(request,'main_app/projects.html', context)

def projects(request):
    context = {
        "title" : "Projects"
    }
    return render(request,'main_app/projects.html', context)

def project(request,slug):
    title = "Uvuru Widows Empowerment"
    if title.split()[0].lower() in slug or title.split()[0].lower() in slug.split('-'):
        context = {
            "title" : title
        }
        return render(request,'main_app/project.html', context)
    else:
        return redirect('projects')