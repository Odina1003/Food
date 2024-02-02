from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request=request, template_name='index.html', context={})

def about(request):
    return render(request=request, template_name='about.html', context={})

def contact(request):
    return render(request=request, template_name='contact.html', context={})

def menu(request):
    breakfast = Breakfast.objects.all()
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()
    desert = Desert.objects.all()
    return render(request=request, template_name='menu.html', context={'breakfast':breakfast, 'lunch':lunch, 'dinner':dinner, 'desert':desert})

def news(request):
    return render(request=request, template_name='news.html', context={})

def news_detail(request):
    return render(request=request, template_name='news-detail.html', context={})
