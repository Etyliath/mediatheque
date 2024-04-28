from django.db import models

class Media(models.Model):
    title = models.CharField('Titre', max_length=200)
    available = models.BooleanField('Disponible', default=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Book(Media):
    author = models.CharField( 'Auteur', max_length=150)
    
    class Meta:
        verbose_name = "livre"

class Dvd(Media):
    realizator = models.CharField( 'Réalisateur', max_length=150)
    
    class Meta:
        verbose_name = "DVD"

class Cd(Media):
    artist = models.CharField('Artiste', max_length=150)
    
    class Meta:
        verbose_name = "CD"

class BoardGame(models.Model):
    name = models.CharField('Nom', max_length=200)
    creator = models.CharField('Créateur', max_length=150)
    available = models.BooleanField('Disponible', default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Jeu de Plateau"

class Member(models.Model):
    name = models.CharField('Nom', max_length=150)
    email = models.EmailField('Mail', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Membre"


class Emprunt(models.Model):
    
    class State(models.TextChoices):
        encours = 'encours',
        rendu = 'rendu'
    
    date_emprunt = models.DateField(auto_now=True)
    date_restitution = models.DateField(null=True)
    lock = models.BooleanField(default=False)
    state = models.CharField(choices=State.choices,max_length=15)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    
    class Meta:
        abstract = True

class EmpruntBook(Emprunt):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.title
    
    class Meta:
        verbose_name = "Emprunt livre"

class EmpruntDvd(Emprunt):
    dvd = models.OneToOneField(Dvd, on_delete=models.CASCADE)
    def __str__(self):
        return self.dvd.title
    
    class Meta:
        verbose_name = "Emprunt DVD"

class EmpruntCd(Emprunt):
    cd = models.OneToOneField(Cd, on_delete=models.CASCADE)
    def __str__(self):
        return self.cd.title
    
    class Meta:
        verbose_name = "Emprunt CD"

class EmpruntBoardGame(Emprunt):
    boardGame = models.OneToOneField(BoardGame, on_delete=models.CASCADE)
    def __str__(self):
        return self.boardGame.title

    class Meta:
        verbose_name = "Emprunt Jeu Plateau"