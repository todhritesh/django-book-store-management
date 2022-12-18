from django.shortcuts import render
from .models import *
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
    data = {
        "categories" : Category.objects.all()
    }
    return render(req,"add_book.html",data)
