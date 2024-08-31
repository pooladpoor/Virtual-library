from django.db import models
from django.contrib.auth import get_user_model

import accounts.models


class Book(models.Model):
    donator = models.ForeignKey(accounts.models.MyUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="donateds")
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    published = models.DateTimeField(auto_now_add=True)
    Summary = models.TextField(blank=True,null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    

