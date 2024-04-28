from django.shortcuts import render,get_object_or_404
from .models import Book, Dvd, Cd, BoardGame, Member
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MemberForm, BookForm, DvdForm, CdForm,EmpruntBook, EmpruntDvd, EmpruntCd, EmpruntBoardGame, BoardGameForm, EmpruntBookForm, EmpruntDvdForm, EmpruntCdForm, EmpruntBoardGameForm

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


def listing_emprunt(request):
    emprunt_books = EmpruntBook.objects.all()
    emprunt_dvds = EmpruntDvd.objects.all()
    emprunt_cds = EmpruntCd.objects.all()
    emprunt_boardgames = EmpruntBoardGame.objects.all()

    return render(request, "bibliothecaire/emprunt/listing.html", {
        'empruntbooks': emprunt_books,
        'empruntdvds': emprunt_dvds,
        'empruntcds' : emprunt_cds,
        'empruntboardgames' : emprunt_boardgames
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

def member_listing(request):
    members = Member.objects.all()
    return render(request, "bibliothecaire/member/listing.html", {'members' : members})

def detail_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    form = MemberForm(instance = member)
    return render(request, "bibliothecaire/member/detail.html",{
        'form': form,
    })


def book_create(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BookForm()
    
    return render(request,"bibliothecaire/book/create.html", {'form': form} )

def detail_book(request, book_id):
    
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(instance = book)
    return render(request, "bibliothecaire/book/detail.html",{
        'form': form,
    })


def dvd_create(request):
    
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            dvd = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = DvdForm()
    
    return render(request,"bibliothecaire/dvd/create.html", {'form': form} )


def detail_dvd(request, dvd_id):
    
    dvd = get_object_or_404(Dvd, pk=dvd_id)
    form = DvdForm(instance = dvd)
    return render(request, "bibliothecaire/dvd/detail.html",{
        'form': form,
    })



def cd_create(request):
    
    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            cd = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = CdForm()
    
    return render(request,"bibliothecaire/cd/create.html", {'form': form} )


def detail_cd(request, cd_id):
    
    cd = get_object_or_404(Cd, pk=cd_id)
    form = CdForm(instance = cd)
    return render(request, "bibliothecaire/cd/detail.html",{
        'form': form,
    })



def boardgame_create(request):
    
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            boardgame = form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BoardGameForm()
    
    return render(request,"bibliothecaire/boardgame/create.html", {'form': form} )

def detail_boardgame(request, boardgame_id):
    
    boardgame = get_object_or_404(BoardGame, pk=boardgame_id)
    form = BoardGameForm(instance = boardgame)
    return render(request, "bibliothecaire/boardgame/detail.html",{
        'form': form,
    })



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

def emprunt_dvd_create(request):
    if request.method == 'POST':
        form = EmpruntDvdForm(request.POST)
        if form.is_valid():
            empruntdvd = form.save()
            dvd = empruntdvd.dvd
            dvd.available = False
            dvd.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = EmpruntDvdForm()
    
    return render(request,"bibliothecaire/dvd/emprunt.html", {'form': form} )


def emprunt_cd_create(request):
    if request.method == 'POST':
        form = EmpruntCdForm(request.POST)
        if form.is_valid():
            empruntcd = form.save()
            cd = empruntcd.cd
            cd.available = False
            cd.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = EmpruntCdForm()
    
    return render(request,"bibliothecaire/cd/emprunt.html", {'form': form} )

def emprunt_boardgame_create(request):
    if request.method == 'POST':
        form = EmpruntBoardGameForm(request.POST)
        if form.is_valid():
            empruntboardgame = form.save()
            boardGame = empruntboardgame.boardGame
            boardGame.available = False
            boardGame.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = EmpruntBoardGameForm()
    
    return render(request,"bibliothecaire/boardgame/emprunt.html", {'form': form} )
