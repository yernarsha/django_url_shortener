from django.urls import path

from . import views

urlpatterns = [
    path('', views.urlShort, name='home'),
    path("<str:slugs>", views.urlRedirect, name="slug")
]
