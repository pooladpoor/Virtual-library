from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model
from home.models import Book
from datetime import datetime


user = get_user_model()


class Borrow(models.Model):
    Borrower = models.ForeignKey(user, on_delete=models.CASCADE, related_name="borrows")
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="borrows")
    s_deadline = models.DateTimeField(auto_now_add=True)
    e_deadline = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.e_deadline:
            self.e_deadline = datetime.now() + timedelta(weeks=1)
        super().save(*args, **kwargs)


class Report(models.Model):
    for_borrow = models.ForeignKey(Borrow, on_delete=models.DO_NOTHING, related_name="reports_borrow",null=True,blank=True)
    to_user = models.ForeignKey(user, on_delete=models.DO_NOTHING, related_name="reports_to",null=True,blank=True)
    titel = models.CharField(max_length=40)
    description = models.TextField()
    dete = models.DateTimeField(auto_now_add=True)