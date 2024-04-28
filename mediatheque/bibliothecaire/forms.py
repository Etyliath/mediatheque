from django import forms

from bibliothecaire.models import Book, Dvd, Cd, BoardGame, Member, EmpruntBook, EmpruntDvd, EmpruntCd, EmpruntBoardGame

class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = '__all__'


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        

class DvdForm(forms.ModelForm):
    
    class Meta:
        model = Dvd
        fields = '__all__'
        


class CdForm(forms.ModelForm):
    
    class Meta:
        model = Cd
        fields = '__all__'
        

class BoardGameForm(forms.ModelForm):
    
    class Meta:
        model = BoardGame
        fields = '__all__'
        


class EmpruntBookForm(forms.ModelForm):
    
    class Meta:
        model = EmpruntBook
        fields = '__all__'
        

class EmpruntDvdForm(forms.ModelForm):
    
    class Meta:
        model = EmpruntDvd
        fields = '__all__'


class EmpruntCdForm(forms.ModelForm):
    
    class Meta:
        model = EmpruntCd
        fields = '__all__'


class EmpruntBoardGameForm(forms.ModelForm):
    
    class Meta:
        model = EmpruntBoardGame
        fields = '__all__'