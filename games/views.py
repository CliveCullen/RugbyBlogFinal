from django.shortcuts import render, HttpResponse, get_object_or_404
from models import team
from models import game
from django.db.models import Q


# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()

    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)

    games = game.objects.filter(teamA=teamOne.Name)

    return render(request, 'home.html', {'teamOne': teamOne, 'teamTwo': teamTwo, 'games':games})

