from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    project_images = [project.image1, project.image2, project.image3, project.image4, project.image5]
    context = {"project": project, "project_images": project_images}
    return render(request, "projects/project_detail.html", context)
