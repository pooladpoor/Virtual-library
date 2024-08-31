from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Borrow)
class BookAdmin(admin.ModelAdmin):
    list_display = ["book","Borrower","e_deadline"]
    
    
@admin.register(Report)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['titel','to_user',"dete"]