from profile.models import ResumeEducation, ResumeExperience, ResumeSkill, ResumeSummary

from django.shortcuts import render


def home(request):
    resume_summary = ResumeSummary.objects.first()
    resume_education = ResumeEducation.objects.all()
    technical_skills = ResumeSkill.objects.filter(category="Technical Skills")
    languages = ResumeSkill.objects.filter(category="Languages")
    resume_experience = ResumeExperience.objects.all()
    context = {
        "summary": resume_summary,
        "education": resume_education,
        "technical_skills": technical_skills,
        "language_skills": languages,
        "experience": resume_experience,
    }
    return render(request, "profile/resume.html", context)