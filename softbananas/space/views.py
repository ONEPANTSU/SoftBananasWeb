from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        "title": "Главная страница",
        "values": ["Soft", "Bananas", "inc."],
        "obj": {
            "OneResident": "Application by AndroidStudio",
            "SawBirzha": "Telegram Bot by aiogram lib",
        },
    }
    return render(request, "space/index.html", data)


def about(request):
    return render(request, "space/about.html")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOOOOOT FOUND! :c</h1>")
