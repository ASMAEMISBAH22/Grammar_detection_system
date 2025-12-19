
"""urlpatterns = [
    path('', views.index, name='index'),               # La page d'accueil
]"""
from django.urls import path
from .views import correct_text_view, index_view  # <--- C'EST CETTE LIGNE QUI MANQUE OU QUI EST FAUSSE !

from grammar_checker import views
urlpatterns = [
    # La page d'accueil (chemin vide '')
    path('', index_view, name='home'),
    path('api/correct/', correct_text_view, name='correct_text'),
]