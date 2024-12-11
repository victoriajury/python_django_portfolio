from profile.models import ResumeSummary

from django.shortcuts import render
from projects.models import IMAGE_COUNT, Project


def project_index(request):
    projects = Project.objects.all().order_by("-date")
    resume_summary = ResumeSummary.objects.first()
    context = {"projects": projects, "summary": resume_summary}
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    project_images = [project.__getattribute__(f"image{i}") for i in range(1, IMAGE_COUNT + 1)]
    resume_summary = ResumeSummary.objects.first()
    context = {"project": project, "project_images": project_images, "summary": resume_summary}
    return render(request, "projects/project_detail.html", context)
