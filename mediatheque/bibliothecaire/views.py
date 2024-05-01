from django.shortcuts import render,get_object_or_404
from .models import Book, Dvd, Cd, BoardGame, Member
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MemberForm, BookForm, DvdForm, CdForm,EmpruntBook, EmpruntDvd, EmpruntCd, EmpruntBoardGame, BoardGameForm, EmpruntBookForm, EmpruntDvdForm, EmpruntCdForm, EmpruntBoardGameForm

def index(request):
    return render(request, "bibliothecaire/index.html")


    """_summary_listing all media
    """
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

    """_summary_listing all emprunt
    """


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

    """Views Member
    """

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
    if request.method == 'POST':
        form = MemberForm(request.POST,instance = member)
        if form.is_valid():
            member = form.save(commit=False)
            member.name = form.cleaned_data['name']
            member.email = form.cleaned_data['email']
            member.save()
            return HttpResponseRedirect('/bibliothecaire/member')
    else:
        form = MemberForm(instance = member)
    return render(request, "bibliothecaire/member/detail.html",{
        'form': form,
    })

def delete_member(request, member_id):
    memeber = Member.objects.get(pk=member_id)
    memeber.delete()
    return HttpResponseRedirect('/bibliothecaire/member/')


    """Book
    """


def create_book(request):
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
    if request.method == 'POST':
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            book = form.save(commit=False)
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.available = form.cleaned_data['available']
            book.save()
            return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BookForm(instance = book)
    return render(request, "bibliothecaire/book/detail.html",{
        'form': form,
    })


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect('/bibliothecaire')


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
    if request.method == 'POST':
        form = DvdForm(request.POST,instance = dvd)
        if form.is_valid():
            dvd = form.save(commit=False)
            dvd.title = form.cleaned_data['title']
            dvd.realizator = form.cleaned_data['realizator']
            dvd.available = form.cleaned_data['available']
            dvd.save()
            return HttpResponseRedirect('/bibliothecaire')
    else:
        form = DvdForm(instance = dvd)
    return render(request, "bibliothecaire/dvd/detail.html",{
        'form': form,
    })


def delete_dvd(request, dvd_id):
    dvd = Dvd.objects.get(pk=dvd_id)
    dvd.delete()
    return HttpResponseRedirect('/bibliothecaire')


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
    if request.method == 'POST':
        form = CdForm(request.POST,instance = cd)
        if form.is_valid():
            cd = form.save(commit=False)
            cd.title = form.cleaned_data['title']
            cd.artist = form.cleaned_data['artist']
            cd.available = form.cleaned_data['available']
            cd.save()
            return HttpResponseRedirect('/bibliothecaire')
    else:
        form = CdForm(instance = cd)
    return render(request, "bibliothecaire/cd/detail.html",{
        'form': form,
    })


def delete_cd(request, cd_id):
    cd = Cd.objects.get(pk=cd_id)
    cd.delete()
    return HttpResponseRedirect('/bibliothecaire')


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
    if request.method == 'POST':
        form = BoardGameForm(request.POST,instance = boardgame)
        if form.is_valid():
            boardgame = form.save(commit=False)
            boardgame.name = form.cleaned_data['name']
            boardgame.creator = form.cleaned_data['creator']
            boardgame.available = form.cleaned_data['available']
            boardgame.save()
            return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BoardGameForm(instance = boardgame)
    return render(request, "bibliothecaire/boardgame/detail.html",{
        'form': form,
    })


def delete_boardgame(request, boardgame_id):
    boardgame = BoardGame.objects.get(pk=boardgame_id)
    boardgame.delete()
    return HttpResponseRedirect('/bibliothecaire')



def create_emprunt_book(request):
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


def detail_emprunt_book(request, empruntbook_id):
    empruntbook = EmpruntBook.objects.get(pk=empruntbook_id)
    if request.method == 'POST':
        form = EmpruntBookForm(request.POST,instance=empruntbook)
        if form.is_valid():
            empruntbook = form.save(commit=False)
            empruntbook.date_restitution = form.cleaned_data['date_restitution']
            empruntbook.lock = form.cleaned_data['lock']
            empruntbook.State = form.cleaned_data['state']
            empruntbook.member = form.cleaned_data['member']
            empruntbook.book = form.cleaned_data['book']
            if empruntbook.state == 'rendu':
                book = empruntbook.book
                book.available = True
                book.save()
            empruntbook.save()
            return HttpResponseRedirect('/bibliothecaire/emprunt')
    else:
        form = EmpruntBookForm(instance=empruntbook)
    return render(request, "bibliothecaire/emprunt/detail.html",{
        'form': form,
    })


def delete_emprunt_book(request, empruntbook_id):
    empruntbook = EmpruntBook.objects.get(pk=empruntbook_id)
    book = empruntbook.book
    book.available = True
    book.save()
    empruntbook.delete()
    
    return HttpResponseRedirect('/bibliothecaire/emprunt')


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

def detail_emprunt_dvd(request, empruntdvd_id):
    empruntdvd = EmpruntDvd.objects.get(pk=empruntdvd_id)
    if request.method == 'POST':
        form = EmpruntDvdForm(request.POST,instance=empruntdvd)
        if form.is_valid():
            empruntdvd = form.save(commit=False)
            empruntdvd.date_restitution = form.cleaned_data['date_restitution']
            empruntdvd.lock = form.cleaned_data['lock']
            empruntdvd.state = form.cleaned_data['state']
            empruntdvd.member = form.cleaned_data['member']
            empruntdvd.dvd = form.cleaned_data['dvd']
            if empruntdvd.state == 'rendu':
                dvd = empruntdvd.dvd
                dvd.available = True
                dvd.save()
            empruntdvd.save()
            return HttpResponseRedirect('/bibliothecaire/emprunt')
    else:
        form = EmpruntDvdForm(instance=empruntdvd)
    return render(request, "bibliothecaire/emprunt/detail.html",{
        'form': form,
    })

def delete_emprunt_dvd(request, empruntdvd_id):
    empruntdvd = EmpruntDvd.objects.get(pk=empruntdvd_id)
    dvd = empruntdvd.dvd
    dvd.available = True
    dvd.save()
    empruntdvd.delete()
    
    return HttpResponseRedirect('/bibliothecaire/emprunt')


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


def detail_emprunt_cd(request, empruntcd_id):
    empruntcd = EmpruntCd.objects.get(pk=empruntcd_id)
    if request.method == 'POST':
        form = EmpruntCdForm(request.POST,instance=empruntcd)
        if form.is_valid():
            empruntcd = form.save(commit=False)
            empruntcd.date_restitution = form.cleaned_data['date_restitution']
            empruntcd.lock = form.cleaned_data['lock']
            empruntcd.state = form.cleaned_data['state']
            empruntcd.member = form.cleaned_data['member']
            empruntcd.cd = form.cleaned_data['cd']
            if empruntcd.state == 'rendu':
                cd = empruntcd.cd
                cd.available = True
                cd.save()
            empruntcd.save()
            return HttpResponseRedirect('/bibliothecaire/emprunt')
    else:
        form = EmpruntCdForm(instance=empruntcd)
    return render(request, "bibliothecaire/emprunt/detail.html",{
        'form': form,
    })


def delete_emprunt_cd(request, empruntcd_id):
    empruntcd = EmpruntCd.objects.get(pk=empruntcd_id)
    cd = empruntcd.cd
    cd.available = True
    cd.save()
    empruntcd.delete()
    return HttpResponseRedirect('/bibliothecaire/emprunt')


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


def detail_emprunt_boardgame(request, empruntboardgame_id):
    empruntboardgame = EmpruntBoardGame.objects.get(pk=empruntboardgame_id)
    if request.method == 'POST':
        form = EmpruntBoardGameForm(request.POST,instance=empruntboardgame)
        if form.is_valid():
            empruntboardgame = form.save(commit=False)
            empruntboardgame.date_restitution = form.cleaned_data['date_restitution']
            empruntboardgame.lock = form.cleaned_data['lock']
            empruntboardgame.state = form.cleaned_data['state']
            empruntboardgame.member = form.cleaned_data['member']
            empruntboardgame.boardGame = form.cleaned_data['boardGame']
            if empruntboardgame.state == 'rendu':
                boardgame = empruntboardgame.boardGame
                boardgame.available = True
                boardgame.save()
            empruntboardgame.save()
            return HttpResponseRedirect('/bibliothecaire/emprunt')
    else:
        form = EmpruntBoardGameForm(instance=empruntboardgame)
    return render(request, "bibliothecaire/emprunt/detail.html",{
        'form': form,
    })


def delete_emprunt_boardgame(request, empruntboardgame_id):
    empruntboardgame = EmpruntBoardGame.objects.get(pk=empruntboardgame_id)
    boardgame = empruntboardgame.boardGame
    boardgame.available = True
    boardgame.save()
    empruntboardgame.delete()
    return HttpResponseRedirect('/bibliothecaire/emprunt')

