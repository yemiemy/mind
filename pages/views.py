from django.shortcuts import render
from accounts.models import Team
from projects.models import Project, Issue
from django.shortcuts import render, get_object_or_404, redirect

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
    submitted = Project.objects.filter(is_submitted=True)
    issues = Issue.objects.all().order_by('-post_date')
    context = {
        'submitted':submitted,
        'issues':issues,
    }
    return render(request, 'projects/notifications.html', context)
def solutions_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'projects/solution-page.html', context)