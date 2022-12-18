from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'eg: Bimal Jalal'}),
            'price': forms.TextInput(attrs={'placeholder': 'eg: 345'}),
            'discount': forms.TextInput(attrs={'placeholder': 'eg: 4'}),
            'title': forms.TextInput(attrs={'placeholder': 'eg: The India Story'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'eg: Write book description here','rows':'4'}),
        }
        fields = "__all__"