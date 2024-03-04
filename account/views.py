from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate
from main.models import Location

from opencage.geocoder import OpenCageGeocode
from django.conf import settings

key = settings.GEOCODER_API
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(44.8303087, -0.5761911)
print(results[0]["formatted"])

def signup(request:HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("account:login")

    else:
        form = UserRegistrationForm()

    return render(request,"account/signup.html",{"form":form})

def signin(request:HttpRequest):
    if request.method == "POST":
       username =  request.POST.get("username")
       password = request.POST.get("password")

       longitude = request.POST.get("longitude")
       latitude = request.POST.get("latidude")

       user = authenticate(request,username=username,password=password)

       if user is not None:
           login(request,user)
           location = geocoder.reverse_geocode(logitude,latitude)
           Location.objects.create(user=request.user,location=location)


