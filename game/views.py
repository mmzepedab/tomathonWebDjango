from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. This is the rank")
    return render(request, 'game/index.html')