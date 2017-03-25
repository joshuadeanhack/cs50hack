from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def makeCode():
    return "It works, Hello, world. You're at the polls index. <br> <h1>Woo</h1>"



def index(request):
    responce = HttpResponse(makeCode())
    return responce
