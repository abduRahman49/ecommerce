from django.urls import path
from .views import hello, client_infos, process_test_request, HomeView, index,get_client

urlpatterns = [
    path('hello/', hello, name="hello"),
    path('commande-infos/<int:id>/', client_infos, name="commandes"),
    path('test-request/', process_test_request, name="test-request"),
    path('cb-view/', HomeView.as_view(), name="cb-view"),
    path('home/', index, name="home"),
    path('catalog/<int:id>', get_client, name="catalog"),
]
