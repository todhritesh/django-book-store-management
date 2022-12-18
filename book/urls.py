from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("single_view/<int:id>",singleView , name="single_view") ,
    path("add_book.html/",addBook , name="add_book")
]
