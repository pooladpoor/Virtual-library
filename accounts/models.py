from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

import home.models

class MyUser(AbstractBaseUser):
    full_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True,default=None)
    adress = models.CharField(max_length=255)
    national_code = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined=models.DateField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = "national_code"
    REQUIRED_FIELDS = ["full_name","phone", "adress"]

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Otp(models.Model):
    nation_code = models.CharField(max_length=10)
    otp_code = models.CharField(max_length=4)
