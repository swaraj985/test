from django.shortcuts import render
from django.http import HttpResponse


def myapp(request):
    return HttpResponse("Hello world")
    # pass


