from django.shortcuts import render
from forms import HeadToHead

from django.http import HttpResponse
# Create your views here.
def index(request):
    form = HeadToHead()

    return render(request,"home.html", {'form': form})