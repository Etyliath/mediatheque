from django.shortcuts import render
from django.urls import path

from . import views


urlpatterns = [
    path("", views.listing, name="listing"),
    path("member/<int:member_id>", views.detail_member, name="detail-member"),
    path("member/", views.member_listing, name="member-listing"),
    path("member/add/", views.member_create, name="member-create"),
    path("member/delete/<int:member_id>", views.delete_member, name="delete-member"),
    path("book/<int:book_id>" , views.detail_book, name="detail-book"),
    path("book/add/", views.create_book, name="create-book"),
    path("book/delete/<int:book_id>", views.delete_book, name="delete-book"),
    path("dvd/<int:dvd_id>", views.detail_dvd, name="detail-dvd"),
    path("dvd/add/", views.dvd_create, name="dvd-create"),
    path("dvd/delete/<int:dvd_id>", views.delete_dvd, name="delete-dvd"),
    path("cd/<int:cd_id>", views.detail_cd, name="detail-cd"),
    path("cd/add/", views.cd_create, name="cd-create"),
    path("cd/delete/<int:cd_id>", views.delete_cd, name="delete-cd"),
    path("boardgame/<int:boardgame_id>", views.detail_boardgame, name="detail-boardgame"),
    path("boardgame/add/", views.boardgame_create, name="boardgame-create"),
    path("boardgame/delete/<int:boardgame_id>", views.delete_boardgame, name="delete-boardgame"),
    path("emprunt/", views.listing_emprunt, name='listing-emprunt'),
    path("empruntbook/<int:empruntbook_id>", views.detail_emprunt_book, name="detail-emprunt-book"),
    path("empruntbook/add/", views.create_emprunt_book, name="create-emprunt-book"),
    path("empruntbook/delete/<int:empruntbook_id>", views.delete_emprunt_book, name="delete-emprunt-book"),
    path("empruntdvd/<int:empruntdvd_id>", views.detail_emprunt_dvd, name="detail-emprunt-dvd"),
    path("empruntdvd/add/", views.emprunt_dvd_create, name="emprunt-dvd-create"),
    path("empruntdvd/delete/<int:empruntdvd_id>", views.delete_emprunt_dvd, name="delete-emprunt-dvd"),
    path("empruntcd/<int:empruntcd_id>", views.detail_emprunt_cd, name="detail-emprunt-cd"),
    path("empruntcd/add/", views.emprunt_cd_create, name="emprunt-cd-create"),
    path("empruntcd/delete/<int:empruntcd_id>", views.delete_emprunt_cd, name="delete-emprunt-cd"),
    path("empruntboardgame/<int:empruntboardgame_id>", views.detail_emprunt_boardgame, name="detail-emprunt-boardgame"),
    path("empruntboardgame/add/", views.emprunt_boardgame_create, name="emprunt-boardgame-create"),
    path("empruntboardgame/delete/<int:empruntboardgame_id>", views.delete_emprunt_boardgame, name="delete-emprunt-boardgame"),

]
