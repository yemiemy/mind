from django.shortcuts import render
from accounts.models import Team

# Create your views here.
def dashboard(request):
    context = {    }
    return render(request, 'accounts/dashboard.html', context)

def create_team(request):
    if request.POST:
        name = request.POST['name']
        members = request.POST['members']
        program_manager = request.POST['program_manager']

        team = Team.objects.create(name=name, members=members, program_manager=program_manager)

        team.save()

    context = {}
    return render(request, 'accounts/create-team.html', context)