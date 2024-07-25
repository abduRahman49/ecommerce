from django.urls import path
from .views import signin_view, signup_view, logout_view


urlpatterns = [
    path('authentication/signup', signup_view, name="signup"),
    path('authentication/signin', signin_view, name="login"),
    path('authentication/logout', logout_view, name="logout"),
]
