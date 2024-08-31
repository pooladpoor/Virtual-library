from django.contrib import admin
from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
 
    path('user_detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('forget_password1/', ForgetPassword1.as_view(), name='forget_password1'),
    path('forget_password2/<str:n_code>', ForgetPassword2.as_view(), name='forget_password2'),
    path('change_password/<str:n_code>', ChangePassword.as_view(), name='change_password'),
  
]

