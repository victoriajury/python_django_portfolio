from django.contrib import admin
from pages.models import ResumeEducation, ResumeExperience, ResumeSkill, ResumeSummary


class ResumeAdminSummary(admin.ModelAdmin):
    list_display = ["name", "address"]


class ResumeAdminEducation(admin.ModelAdmin):
    list_display = ["location", "date_attended"]


class ResumeAdminSkills(admin.ModelAdmin):
    list_display = ["skill", "category"]


class ResumeAdminExperience(admin.ModelAdmin):
    list_display = ["role", "date_attended", "location"]


admin.site.register(ResumeSummary, ResumeAdminSummary)
admin.site.register(ResumeEducation, ResumeAdminEducation)
admin.site.register(ResumeSkill, ResumeAdminSkills)
admin.site.register(ResumeExperience, ResumeAdminExperience)
