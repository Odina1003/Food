from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html', context={})

def about(request):
    return render(request=request, template_name='about.html', context={})

def contact(request):
    return render(request=request, template_name='contact.html', context={})

def menu(request):
    return render(request=request, template_name='menu.html', context={})

def news(request):
    return render(request=request, template_name='news.html', context={})

def news_detail(request):
    return render(request=request, template_name='news_detail.html', context={})

def home(request):
    return HttpResponse('This is home page')