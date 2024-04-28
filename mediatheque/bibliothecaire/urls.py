from django.shortcuts import render
from django.urls import path

from . import views


urlpatterns = [
    path("", views.listing, name="listing"),
    path("<int:book_id>" , views.detail_book, name="detail-book"),
    path("member/<int:member_id>", views.member_delete, name="member-delete"),
    path("member/", views.member_listing, name="member-listing"),
    
    path("member/add/", views.member_create, name="member-create"),
    path("book/add/", views.book_create, name="book-create"),
    path("dvd/add/", views.dvd_create, name="dvd-create"),
    path("cd/add/", views.cd_create, name="cd-create"),
    path("boardgame/add/", views.boardgame_create, name="boardgame-create"),
    path("empruntbook/add/", views.emprunt_book_create, name="emprunt-book-create")
    # path("<int:id>", views.detail, name="detail"),

]
