from django.shortcuts import render,get_object_or_404
from .models import Book, Dvd, Cd, BoardGame
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookForm, EmpruntBookForm

def index(request):
    return render(request, "bibliothecaire/index.html")


def listing(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()

    return render(request, "bibliothecaire/listing.html", {
        'books': books,
        'dvds': dvds,
        'cds' : cds,
        'boardgames' : boardgames
        })
    
    
def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, "bibliothecaire/book/detail.html",context)


def book_create(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BookForm()
    
    return render(request,"bibliothecaire/book/create.html", {'form': form} )

def emprunt_book_create(request):
    if request.method == 'POST':
        form = EmpruntBookForm(request.POST)
        if form.is_valid():
            empruntbook = form.save()
            book = empruntbook.book
            book.available = False
            book.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = EmpruntBookForm()
    
    return render(request,"bibliothecaire/book/create.html", {'form': form} )