from django.urls import path
from .views import hello, client_infos, process_test_request, HomeView

urlpatterns = [
    path('hello/', hello),
    path('commande-infos/<int:id>/', client_infos),
    path('test-request/', process_test_request),
    path('cb-view/', HomeView.as_view()),
]
