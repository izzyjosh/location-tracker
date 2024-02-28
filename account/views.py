from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import UserRegistrationForm

def signup(request:HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("account:login")

    else:
        form = UserRegistrationForm()

    return render(request,"account/signup.html",{"form":form})

