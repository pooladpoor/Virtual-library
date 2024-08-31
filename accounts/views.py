import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .models import Otp
from home.models import Book
from .forms import *
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .sms import send_sms

user = get_user_model()  # اون مودل یوزر که تو تنظیمات فعال هست


# مشخصات کاربر رو نشون میده
class UserDetail(View):
    def get(self, request, pk):
        context = {
            "user": get_object_or_404(user, id=pk)
        }
        return render(request, 'accounts/user_detail.html', context=context)


# لیست همه کاربر ها
class UserList(View):
    def get(self, request):
        context = {
            "users": user.objects.all()
        }
        return render(request, 'accounts/user_list.html', context=context)


class Login(View):
    form_class = LoginForm
    template_name = "accounts/login_form.html"
    cotext = {
        "form_title": "Log in",
        "form": form_class,
        "Button_text": "log in",
    }
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.cotext)
    
    def post(self, request, *args, **kwargs):
        national_code = request.POST['national_code']
        password = request.POST['password']
        usera = authenticate(request, national_code=national_code, password=password)
        if usera is not None:
            login(request, usera)
            messages.success(request, "You are logged in", "success")
            next_url = request.GET.get('next', reverse("home:book_list"))
            return redirect(next_url)
        else:
            messages.error(request, "The national code or password is wrong", "danger ")
            return render(request, self.template_name, self.cotext)


@login_required
def Logout(request):
    logout(request)
    messages.success(request, "You are logged out", "success")
    return redirect('home:book_list')


class Signup(View):
    form_class = SignupForm
    template_name = "form.html"
    cotext = {
        "form_title": "Sign up",
        "form": form_class,
        "Button_text": "sign up",
    }
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.cotext)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have signed up", "success")
            return redirect('home:book_list')
        else:
            self.cotext["form"] = form
        return render(request, self.template_name, self.cotext)


#  کد ملی کاربر رو برای تعویض رمز میگیره و اون رو به کلاس بعدی پاس میده
class ForgetPassword1(View):
    form = ForgetPasswordForm1
    
    def get(self, request):
        return render(request, "accounts/forget_password1.html", {"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            n_code = form.cleaned_data['code']
            return redirect("accounts:forget_password2", n_code=n_code)
        else:
            return render(request, "accounts/forget_password1.html", {"form": form})


# به شماره کاربر پیامک حاوی کد تایید میفرسته و کد رو از کاربر میگیره
# اگه درست بود اون رو به کلاس بعدی پاس میده تا روز جدید رو انتخاب کنه
class ForgetPassword2(View):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phone = None
        self.myuser = None
        self.form = None
    
    def setup(self, request, *args, **kwargs):
        self.form = ForgetPasswordForm2
        self.myuser = get_object_or_404(user, national_code=kwargs['n_code'])
        self.phone = self.myuser.phone
        super().setup(request, *args, **kwargs)
    
    def get(self, request, n_code):
        try: # اگه از قبل کدی وجود داشته باششه حذفش میکنه
            Otp.objects.get(nation_code=n_code).delete()
        except:
            pass
        random_code = random.randrange(1000, 9999)
        Otp.objects.create(nation_code=n_code, otp_code=random_code)
        send_sms(self.phone, random_code)
        context = {
            "phone": self.phone,
            "form": self.form
        }
        return render(request, "accounts/forget_password2.html", context)
    
    def post(self, request, n_code):
        otp_code1 = Otp.objects.get(nation_code=n_code).otp_code
        otp_code2 = request.POST["code"]
        if otp_code1 == otp_code2:
            context = {"form": ChengePasswordForm,
                       "n_coode": n_code}
            return render(request, "accounts/change_password.html", context)
        else:
            messages.error(request, "code is not corect", extra_tags='danger')
            context = {
                "phone": self.phone,
                "form": self.form
            }
            return render(request, "accounts/forget_password2.html", context)


# رمز جدید رو از کاربر میگیره و رمز رو تغییر میده
class ChangePassword(View):
    def post(self, request, n_code):
        form = ChengePasswordForm(request.POST)
        if form.is_valid():
            my_user = get_object_or_404(user, national_code=n_code)
            my_user.set_password(request.POST["pas1"])
            my_user.save()
            messages.success(request, "Your password changed", "success")
            return redirect("accounts:login")
        else:
            context = {"form": form,
                       "n_coode": n_code}
            return render(request, "accounts/change_password.html", context)
