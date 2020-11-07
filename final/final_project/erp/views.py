from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = 'Las Vegas'
    context = {
        "user": request.user
    }
    return HttpResponseRedirect(reverse("inv-home"))

