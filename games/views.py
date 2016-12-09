from django.shortcuts import render, HttpResponse, get_object_or_404
from models import team, game
from models import overall


# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()

    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)

    games = game.objects.filter(teamA=teamOne.Name, teamB=teamTwo.Name)
    games2 = game.objects.filter(teamA=teamTwo.Name, teamB=teamOne.Name)

    history = get_object_or_404(overall,(teamOneName + " " + teamTwoName + " Overall"))

    return render(request, 'home.html', {'teamOne': teamOne, 'teamTwo': teamTwo, 'games': games, 'games2': games2, 'overall':history})



