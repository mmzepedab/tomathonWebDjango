from django.shortcuts import render

from .models import Rank
from rest_framework import viewsets
from rank.serializers import RankSerializer

from django.core import serializers
from django.http import HttpResponse

from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@ensure_csrf_cookie
def rankList(request):
    #return HttpResponse("Hello, world. This is the rank")
    ranks = Rank.objects.all()
    #return render(request, 'rank/index.html', {'ranks': ranks})
    response = serializers.serialize("json", ranks)
    return HttpResponse(response, content_type='application/json')

def ranks(request):
    ranks = Rank.objects.all()
    return render(request, 'rank/index.html', {'ranks': ranks})

class RankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Rank.objects.all()
    serializer_class = RankSerializer