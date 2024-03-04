from django.shortcuts import render
from .models import Location


def dashboard(request):
    locations = Location.objects.all()[:5]
    print(locations)
    return render(request,"dashboard.html",context={"locations":locations})
