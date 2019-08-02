from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project, Issue
from accounts.models import Team
from django.contrib import messages
from datetime import datetime
import pytz

# Create your views here.
def create(request):
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']
        point = request.POST['point']
        startdate = request.POST['startdate']
        deadline = request.POST['deadline']

        project = Project.objects.create(title=title, description=description, point=point, startdate=startdate, deadline=deadline)

        if 'attachment' in request.FILES:
            attachment = request.FILES['attachment']
            project.attachment = attachment
            
        project.save()

        messages.success(request, 'Project successfully created!')
        redirect ('dashboard')
        
    return render(request, 'projects/create.html')

def projects(request):
    all_projects = Project.objects.all().order_by('-startdate')
    active_projects = Project.objects.all().filter(is_accepted=False)
    accepted_projects = Project.objects.all().filter(is_accepted=True)
    context = {
        'all_projects': all_projects,
        'active_projects': active_projects,
        'accepted_projects': accepted_projects,
    }
    return render(request, 'projects/projects.html', context)

def assign_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.POST:
        team = request.POST['team']
        team = Team.objects.get(id=team)
        project.team = team
        project.save()
        messages.success(request, 'Project successfully assigned!')


    teams = Team.objects.all()

    context={
        "project":project, 'teams':teams,
    }
    return render(request, 'projects/assign-project.html', context)


def submit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.POST:
        utc = pytz.UTC
        deadline = str(project.deadline)
        deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S%z')
        deadline = deadline.replace(tzinfo=utc)
        now = datetime.now()
        now = now.replace(tzinfo=utc)
        project.is_submitted =True
        if now < deadline:
            team = project.team
            team.pendingPoints = project.point
            team.save()
            messages.success(request, 'Congratulations! Project submitted Successfully before deadline!')
            return redirect('dashboard')
        else:
            project.team.pendingPoints = 0
            project.save()
            messages.success(request, "Sorry! Project submitted successfully but you didn't meet the deadline")
            return redirect('dashboard')
    context = {
        'project':project
    }
    return render(request, 'projects/submit-project.html', context)

def confirm_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.POST:
        team = project.team
        team.totalPoints += team.pendingPoints
        team.pendingPoints = 0
        team.save()
        project.is_accepted = True
        project.save()
        messages.success(request, 'Project confirmed and leaderboard updated successfully')

        return redirect('dashboard')

    context = {
        'project': project,
    }

    return render(request, 'projects/confirm-project.html', context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.POST:
        project.delete()
        messages.success(request, 'Project successfully deleted!')
        return redirect('dashboard')

    context = {
        'project':project
    }
    return render(request, 'projects/delete-project.html', context)

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.POST:
        project.title = request.POST['title']
        project.description = request.POST['description']
        project.point = request.POST['point']
        project.startdate = request.POST['startdate']
        project.deadline = request.POST['deadline']

        if 'attachment' in request.FILES:
            project.attachment = request.FILES['attachment']
            
        project.save()

        messages.success(request, 'Project successfully Updated!')
        redirect ('dashboard')

    context = {
        'project':project
    }
    return render(request, 'projects/edit-project.html', context)

def issues(request):
    issues = Issue.objects.all().order_by('-post_date')

    context = {
        "issues": issues,
    }
    
    return render(request, 'projects/issues.html', context)

def create_issue(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.POST:
        title = request.POST['title']
        message = request.POST['message']

        issue = Issue.objects.create(title=title, message=message, project=project)
        issue.save()

        messages.success(request, 'Issue successfully created!')

    context = {
        'project':project,
    }
    return render(request, 'projects/create-issue.html', context)

def issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    context = {
        'issue':issue,
    }
    return render(request, 'projects/issue.html', context)
    

