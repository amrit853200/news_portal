from django.shortcuts import render
from .models import *

# Create your views here.
def homeView(request):
    views = {}
    views['navbar'] = navbar.objects.all()
    return render(request, 'index.html', views)
    

def category(request):
    views = {}
    views['navbar'] = navbar.objects.all()

    return render(request, 'categori.html', views)

def aboutView(request):
    views = {}
    return render(request, 'about.html', views)

def latestView(request):
    views = {}
    return render(request, 'latest_news.html', views)

def contactView(request):
    views = {}
    return render(request, 'contact.html', views)

def elementView(request):
    views = {}
    return render(request, 'elements.html', views)

def blogView(request):
    views = {}
    return render(request, 'blog.html', views)

def singleView(request):
    views = {}
    return render(request, 'single-blog.html', views)

def detailsView(request):
    views = {}
    return render(request, 'details.html', views)