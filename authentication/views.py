from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Ce formulaire permet de créer un nouvel utilisateur
        if form.is_valid():
            form.save() # A ce niveau le hashage est géré automatiquement par Django. La méthode save de UserCreationForm va faire appel à une autre méthode set_password qui hashera le mot de passe avant de le sauvegarder
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # Ici vous remarquez qu'il y a comme valeur password1, c'est parce qu'on peut demander deux champs password et les comparer (password1, password2)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Utilisateur créé avec succès')
            return redirect('home')
        else:
            messages.error(request, 'Les données soumises sont invalides')
    else:
        form = CustomUserCreationForm()

    return render(request, "authentication/register.html", {"form": form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # Le formulaire utilisé est utilisé spécifiquement pour l'authentification (Login)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie')
                return redirect('home')
        else:
            messages.error(request, 'Echec connexion, veuillez vérifier vos paramètres')
    else:
        form = AuthenticationForm()

    return render(request, "authentication/signin.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
