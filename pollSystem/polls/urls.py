from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path("candidates/", views.candidates, name="candidates"),
    path("positions/", views.positions, name="positions"),
    path("changepass/", views.changepass, name="changepass"),
    path("registeracc/", views.registeracc, name="registeracc"),
    path("positionsDelete/<mypos>/", views.positionsDelete, name="positionsDelete"),
    path("candidatesDelete/<mycos>/", views.candidatesDelete, name="candidatesDelete"),
    path("Logout/", views.Logout, name="Logout"),
    path("vote/", views.vote, name="vote"),
    path("makevote/<mycos> <mypos>/", views.makevote, name="makevote"),
]
