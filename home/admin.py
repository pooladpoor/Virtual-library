from django.contrib import admin
from .models import *



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name","author","donator","is_available"]


