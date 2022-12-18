from django.shortcuts import render,redirect
from .models import *
from .forms import BookForm
from django.db.models import Q
# Create your views here.

def home(req):
    search_keyword = req.GET.get("q") if req.GET.get("q") else None
    books = ""
    if(search_keyword):
        books = Book.objects.filter(
            Q(title__contains=search_keyword) |
            Q(author__contains=search_keyword)
            )
    else:
        books = Book.objects.all()
    data = {
        "books": books
    }
    return render(req,"home.html",data)

def singleView(req,id):
    data = {
        "book":Book.objects.get(pk=id)
    }
    print(data)
    return render(req,"single_view.html",data)

def addBook(req):
    forms = BookForm()
    data = {
        "categories" : Category.objects.all(),
        "forms":forms
    }
    if req.method=="POST" :
       form = BookForm(req.POST, req.FILES or None)
       if form.is_valid():
        form.save()
        return redirect("home")
    return render(req,"add_book.html",data)
