from django.contrib import admin

from bibliothecaire.models import Member, Book, Dvd, Cd, BoardGame, EmpruntBook, EmpruntDvd, EmpruntCd, EmpruntBoardGame

admin.site.register(Book)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(BoardGame)

admin.site.register(EmpruntDvd)
admin.site.register(EmpruntCd)
admin.site.register(EmpruntBoardGame)

class EmpruntBookInLine(admin.TabularInline):
    readonly_fields = ['date_emprunt']
    model = EmpruntBook
    fieldsets = [
        (None, {'fields' : ['book','date_restitution']})
    ]
    extra = 0

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines = [EmpruntBookInLine,]
    

@admin.register(EmpruntBook)
class EmpruntBook(admin.ModelAdmin):
    readonly_fields = ['date_emprunt']
    