from profile.models import ResumeEducation, ResumeExperience, ResumeSkill, ResumeSummary

from django.contrib import admin


class ResumeAdminSummary(admin.ModelAdmin):
    list_display = ["name", "address"]


class ResumeAdminEducation(admin.ModelAdmin):
    list_display = ["location", "date_attended", "position"]


class ResumeAdminSkills(admin.ModelAdmin):
    list_display = ["skill", "category", "position"]


class ResumeAdminExperience(admin.ModelAdmin):
    list_display = ["role", "date_attended", "location", "position"]


admin.site.register(ResumeSummary, ResumeAdminSummary)
admin.site.register(ResumeEducation, ResumeAdminEducation)
admin.site.register(ResumeSkill, ResumeAdminSkills)
admin.site.register(ResumeExperience, ResumeAdminExperience)
