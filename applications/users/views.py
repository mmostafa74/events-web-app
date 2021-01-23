from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from applications.users.forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect("events")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
