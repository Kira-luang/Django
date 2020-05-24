from django.shortcuts import render, HttpResponse


# Create your views here.


def response(request):
    return HttpResponse('<h1>Hello Dear</h1>')
