from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('menu/', menu, name='menu'),
    path('news/', news, name='news'),
    path('news_detail/', news_detail, name='news-detail'),
]