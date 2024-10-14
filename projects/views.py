from django.shortcuts import render
from projects.models import IMAGE_COUNT, Project


def project_index(request):
    projects = Project.objects.all().order_by("-date")
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    project_images = [project.__getattribute__(f"image{i}") for i in range(1, IMAGE_COUNT + 1)]
    context = {"project": project, "project_images": project_images}
    return render(request, "projects/project_detail.html", context)
