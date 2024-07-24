from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # A ce niveau le hashage est géré automatiquement par Django. La méthode save de UserCreationForm va faire appel à une autre méthode set_password qui hashera le mot de passe avant de le sauvegarder
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # Ici vous remarquez qu'il y a comme valeur password1, c'est parce qu'on peut demander deux champs password et les comparer (password1, password2)
            user = authenticate(username, password)
            login(request, user)
            redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "authenticate/register.html", {"form": form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, "authenticate/signin.html", {"form": form})
