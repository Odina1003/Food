from django.contrib import admin
from .models import *

@admin.register(Breakfast)
class BreakfastAdmin(admin.ModelAdmin):
    list_display = ['image','name','price','ball', 'review']
    list_filter = ['name', 'ball']
@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    list_display = ['image','name','price','ball', 'review']
    list_filter = ['name', 'ball']
@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    list_display = ['image','name','price','ball', 'review']
    list_filter = ['name', 'ball']
@admin.register(Desert)
class DesertAdmin(admin.ModelAdmin):
    list_display = ['image','name','price','ball', 'review']
    list_filter = ['name', 'ball']

