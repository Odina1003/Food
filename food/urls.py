from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('news/', views.news, name='news'),
    path('news_detail/', views.news_detail, name='news-detail'),
]