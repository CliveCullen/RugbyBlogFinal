from django.shortcuts import render, HttpResponse, get_object_or_404
from models import team, game
#from models import overall


# Create your views here.
def head_to_head(request):
    teamOneName = request.GET.get('teamOne').capitalize()
    teamTwoName = request.GET.get('teamTwo').capitalize()

#    h1 = get_object_or_404(overall, Name= teamOneName + " " + teamTwoName + " Overall" )
 #   h2 = get_object_or_404(overall, Name= teamOneName + " " + teamTwoName + " Overall" )


    teamOne = get_object_or_404(team, Name=teamOneName)
    teamTwo = get_object_or_404(team, Name=teamTwoName)

    g1 = game.objects.filter(teamA=teamOne.Name, teamB=teamTwo.Name)
    g2 = game.objects.filter(teamA=teamTwo.Name, teamB=teamOne.Name)

    return render(request,'home.html',{'teamOne':teamOne,'teamTwo':teamTwo,'games':g1,'games2':g2})



