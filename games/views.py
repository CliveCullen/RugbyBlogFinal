from django.shortcuts import render, HttpResponse, get_object_or_404
from models import team, game, history



# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()



    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)

<<<<<<< HEAD
    g1 = game.objects.filter(teamA=teamOne.Name, teamB=teamTwo.Name)
    g2 = game.objects.filter(teamA=teamTwo.Name, teamB=teamOne.Name)

    return render(request,'home.html',{'teamOne':teamOne,'teamTwo':teamTwo,'games':g1,'games2':g2})

=======
    games = game.objects.filter(teamA=teamOne.Name, teamB=teamTwo.Name).order_by("-date")
    games2 = game.objects.filter(teamA=teamTwo.Name, teamB=teamOne.Name).order_by("-date")
>>>>>>> parent of e066c17... still not in order


