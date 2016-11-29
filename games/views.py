from django.shortcuts import render, HttpResponse, get_object_or_404
from models import team
from models import game

# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()

    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)

    # games = Game.objects.filter(teamA = teamOne )

    return render(request, 'home.html', {'teamOne': teamOne,'teamTwo':teamTwo})


def Game(request):
    Game = game.objects.all()
    return render(request, "home.html",{"game":Game})

