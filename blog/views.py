# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # The line below sends a plain text
    # return HttpResponse("Hello World")
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
