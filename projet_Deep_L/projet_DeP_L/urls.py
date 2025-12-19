from django.contrib import admin
from django.urls import path, include
from grammar_checker.views import index_view  # <--- On importe ta vue d'accueil

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. L'API reste sur /api/ (pour que ton bouton "Corriger" continue de marcher)
    path('api/', include('grammar_checker.urls')),
    
    # 2. La page d'accueil à la racine (http://127.0.0.1:8000/)
    path('', index_view, name='home'),
]