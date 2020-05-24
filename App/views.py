from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def response(request):
    return HttpResponse('Hello Kira')


def index(request):
    return render(request, 'index.html')
