from .views import *
from django.urls import path

app_name = 'borrows'

urlpatterns = [
    path('borrow_list', BorrowList.as_view(),name='borrow_list'),
    path('my_borrow_list', MyBorrowList.as_view(),name='my_borrow_list'),
    path('borrow_book/<int:pk>', BorrowBook.as_view(),name='borrow_book'),
    path('report/<int:id_user>/<int:id_borrow>', Report.as_view(), name="report"),
    path('give_back_book/<int:id_book>', GiveBack.as_view(), name="give_back_book"),
    ]
