from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from borrows.models import Borrow
from .models import Book
from .forms import AddBookForm


#  وقتی کاربر فقط آدس سایت رو وارد کنه هدایت میشه به لیست کتاب ها (به عنوان صفحه اصلی)
class Index(View):
    def get(self, request):
        return redirect("home:book_list")


# جزِیات کتاب رو نشون میده (قرض گرفتن کتاب . پس دادن . اطلاعات کاربر قبلی . گزارش کاربر قبلی )
class BookDetail(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        context = {"book": book}
        if not book.is_available:
            borrow = Borrow.objects.filter(book=book).last()
            borrower = borrow.Borrower
            if borrower == request.user:
                context["borrow_id"] = borrow.id
                context["user_id"] = borrower.id
                return render(request, template_name="borrows/borrow_book.html", context=context)
            context["current_borrower"] = borrower
        
        return render(request, 'home/book_detail.html', context=context)


# لیست همه کتاب ها
class BookList(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            "books": books
        }
        return render(request, 'home/book_list.html', context=context)


# اهدا کردن کتاب و اضافه شدن به لیست کتاب ها
class BookCreate(LoginRequiredMixin, View):
    form_class = AddBookForm
    template_name = "form.html"
    
    def get(self, request, *args, **kwargs):
        cotext = {
            "form_title": "Donate Book",
            "form": self.form_class,
            "Button_text": "submit",
        }
        return render(request, self.template_name, cotext)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nwe_book = form.save(commit=False)
            nwe_book.donator = request.user
            nwe_book.save()
            messages.success(request, "Your success message", "success")
            return redirect('home:book_list')
        else:
            cotext = {
                "form_title": "Donate Book",
                "form": form,
                "Button_text": "submit",
            }
            return render(request, self.template_name, cotext)

#-4---

# this is MMMM branch................

#---____________________________________________________