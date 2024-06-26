from django.contrib import admin
from django.urls import path, include
from bibliothecaire import views
from django.conf import settings

urlpatterns = [
    path("", views.index, name='index'),
    path("bibliothecaire/", include("bibliothecaire.urls")),
    path("admin/", admin.site.urls),
]
