from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("Index Page")


def login(request):
    return HttpResponse("<h1>Log In</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOOOOOT FOUND! :c</h1>")