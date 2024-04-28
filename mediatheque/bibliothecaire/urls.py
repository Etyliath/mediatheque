from django.shortcuts import render
from django.urls import path

from . import views


urlpatterns = [
    path("", views.listing, name="listing"),
    path("member/<int:member_id>", views.detail_member, name="detail-member"),
    path("member/", views.member_listing, name="member-listing"),
    path("member/add/", views.member_create, name="member-create"),
    path("book/<int:book_id>" , views.detail_book, name="detail-book"),
    path("book/add/", views.book_create, name="book-create"),
    path("dvd/<int:dvd_id>", views.detail_dvd, name="detail-dvd"),
    path("dvd/add/", views.dvd_create, name="dvd-create"),
    path("cd/<int:cd_id>", views.detail_cd, name="detail-cd"),
    path("cd/add/", views.cd_create, name="cd-create"),
    path("boardgame/<int:boardgame_id>", views.detail_boardgame, name="detail-boardgame"),
    path("boardgame/add/", views.boardgame_create, name="boardgame-create"),
    path("emprunt/", views.listing_emprunt, name='listing-emprunt'),
    path("empruntbook/add/", views.emprunt_book_create, name="emprunt-book-create"),
    path("empruntdvd/add/", views.emprunt_dvd_create, name="emprunt-dvd-create"),
    path("empruntcd/add/", views.emprunt_cd_create, name="emprunt-cd-create"),
    path("empruntboardgame/add/", views.emprunt_boardgame_create, name="emprunt-boardgame-create"),

]
