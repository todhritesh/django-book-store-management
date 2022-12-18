from django.shortcuts import render,redirect
from .models import *
from .forms import BookForm
# Create your views here.

def home(req):
    data = {
        "books":Book.objects.all()
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
