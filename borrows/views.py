from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .forms import ReportForm
from home.models import Book
from borrows.models import Borrow


# قرض گرفتن کتاب
class BorrowBook(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.is_available = False
        book.save()
        borrow_id = Borrow.objects.create(Borrower=request.user, book=book).id
        user_id = request.user.id
        context = {'book': book, "borrow_id": borrow_id, "user_id":user_id}
        
        return render(request, template_name="borrows/borrow_book.html", context=context)


# پس دادن کتابی که قرض گرفته شده
class GiveBack(View):
    def get(self, request, id_book):
        book = get_object_or_404(Book, id=id_book)
        book.is_available = True
        book.save()
        return redirect("home:book_detail", id=id_book)


#  لیست همه تراکنش های قرض گرفتن کتاب
class BorrowList(View):
    def get(self, request):
        context = {
            'borrows': Borrow.objects.all(),
            "all": True
        }
        return render(request, 'borrows/borrow_list.html',context=context)
        
        
# لیست تراکنش های قرض گرفتن هایی که خود کاربر انجام داده
class MyBorrowList(LoginRequiredMixin,View):
    def get(self, request):
        context = {
            'borrows': Borrow.objects.filter(Borrower=request.user),
            "all": False
        }
        return render(request, 'borrows/borrow_list.html',context=context)
 
 
# گزارش قرض گیرنده قبلی کتاب
class Report(LoginRequiredMixin, View):
    form_class = ReportForm
    template_name = "form.html"
    cotext = {
        "form_title": "report",
        "form": form_class,
        "Button_text": "submit",
    }
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.cotext)
    
    def post(self, request, id_user, id_borrow, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            rep = form.save(commit=False)
            rep.to_user = get_object_or_404(get_user_model(),  id=id_user)
            rep.for_borrow = get_object_or_404(Borrow, id=id_borrow)
            rep.save()
            messages.success(request, "Your report has been sent", "success")
            return redirect('home:book_list')
        else:
            return render(request, self.template_name, self.cotext)


