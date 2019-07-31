from django.shortcuts import render, get_object_or_404
from projects.models import Project

# Create your views here.
def create(request):
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']
        point = request.POST['point']
        startdate = request.POST['startdate']
        deadline = request.POST['deadline']

        project = Project.object.create(title=title, description=description, point=point, startdate=startdate, deadline=deadline)

        if 'attachment' in request.FILES:
            attachment = request.FILES['attachment']

        project.attachment = attachment
        project.save()

    return render(request, 'projects/create.html')

def projects(request):
    return render(request, 'projects/projects.html')

def assign_project(request, project_id):
    if request.POST:
        team = request.POST['team']
        project = get_object_or_404(Project, pk=project_id)
        project.team = team
        project.save()
    return render(request, 'projects/assign-project.html')
