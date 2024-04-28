from django.shortcuts import render,get_object_or_404
from .models import Book, Dvd, Cd, BoardGame, Member
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MemberForm, BookForm, DvdForm, CdForm, BoardGameForm, EmpruntBookForm

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
    
    return render(request, "bibliothecaire/book/detail.html",{
        'book': book,
    })


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            book = form.save()
        return HttpResponseRedirect('/bibliothecaire/member/')
    else:
        form = MemberForm()
    return render(request,"bibliothecaire/book/create.html", {'form': form} )


def member_delete(request, member_id):
    member = get_object_or_404(Member, pk =  member_id)
    member.objects.delete()
    return HttpResponseRedirect('/bibliothecaire/member/')


def member_listing(request):
    members = Member.objects.all()
    return render(request, "bibliothecaire/member/listing.html", {'members' : members})


def book_create(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BookForm()
    
    return render(request,"bibliothecaire/book/create.html", {'form': form} )


def dvd_create(request):
    
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            dvd = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = DvdForm()
    
    return render(request,"bibliothecaire/dvd/create.html", {'form': form} )


def cd_create(request):
    
    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            cd = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = CdForm()
    
    return render(request,"bibliothecaire/cd/create.html", {'form': form} )


def boardgame_create(request):
    
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            boardgame = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BoardGameForm()
    
    return render(request,"bibliothecaire/boardgame/create.html", {'form': form} )


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
    
    return render(request,"bibliothecaire/book/emprunt.html", {'form': form} )

