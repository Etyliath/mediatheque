from django import forms

from bibliothecaire.models import Book, EmpruntBook

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        

class EmpruntBookForm(forms.ModelForm):
    
    class Meta:
        model = EmpruntBook
        fields = '__all__'