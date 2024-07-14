from django.urls import path
from .views import hello, client_infos

urlpatterns = [
    path('hello/', hello),
    path('commande-infos/<int:id>', client_infos)
]
