from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils import timezone
from models import team, game
from django.db.models import Q

# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()



    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)


    games = game.objects.filter(teamA=teamOne.Name, teamB=teamTwo.Name)
    games2= game.objects.filter(teamA=teamTwo.Name, teamB=teamOne.Name)

    # games = game.objects.filter(Q(teamA=teamOne.Name, teamB=teamTwo.Name) or Q(teamA=teamTwo.Name, teamB=teamOne.Name))


    return render(request,'home.html',{'teamOne':teamOne,'teamTwo':teamTwo,'games':games,'games2':games2})


