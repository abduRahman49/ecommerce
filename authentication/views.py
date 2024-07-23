from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "authenticate/register.html", {"form": form})
