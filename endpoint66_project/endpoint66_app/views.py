from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("I heard You")


def goGetTheGood(request):
    return HttpResponse("Here you go, Matching Socks")


def happyhappyjoyjoy(request):
    return HttpResponse("I want a beach walk")


