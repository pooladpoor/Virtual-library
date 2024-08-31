from .views import *
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('book_list/', BookList.as_view(), name='book_list'),
    path('book_detail/<int:id> ', BookDetail.as_view(), name='book_detail'),
    path('book_create/', BookCreate.as_view(),name='book_create' ),
    ]
