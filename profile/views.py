from profile.models import ResumeEducation, ResumeExperience, ResumeSkill, ResumeSummary

from django.shortcuts import render


def home(request):
    resume_summary = ResumeSummary.objects.first()
    resume_education = ResumeEducation.objects.all().order_by("position")
    technical_skills = ResumeSkill.objects.filter(category="Technical Skills").order_by("position")
    languages = ResumeSkill.objects.filter(category="Languages").order_by("position")
    resume_experience = ResumeExperience.objects.all().order_by("position")
    context = {
        "summary": resume_summary,
        "education": resume_education,
        "technical_skills": technical_skills,
        "language_skills": languages,
        "experience": resume_experience,
    }
    return render(request, "profile/resume.html", context)
