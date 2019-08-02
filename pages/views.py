from django.shortcuts import render
from accounts.models import Team

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def leaderboard(request):
    teams = Team.objects.all().order_by('-totalPoints')
    length = len(teams)
    n = range(1, length+1)

    dictionary = {}
    position = []

    for x in n:
        position.append(x)

    for key,val in zip(position,teams):
        dictionary[key] = val

    print(dictionary)

    context = {
        'teams': teams, 'dictionary':dictionary,
    }
    return render(request, 'pages/leaderboard.html', context)

def notifications(request):
    context = {
        
    }
    return render(request, 'pages/notifications.html', context)