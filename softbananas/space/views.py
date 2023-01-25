from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Index Page")


def login(request):
    return HttpResponse("<h1>Log In</h1>")
