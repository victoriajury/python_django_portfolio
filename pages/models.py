from django.db import models


class ResumeSummary(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)


class ResumeEducation(models.Model):
    location = models.CharField(max_length=100)
    date_attended = models.CharField(max_length=50)
    study_details = models.TextField()


class ResumeSkill(models.Model):
    category = models.CharField(max_length=100)
    skill = models.CharField(max_length=50)


class ResumeExperience(models.Model):
    role = models.CharField(max_length=100)
    date_attended = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    role_details = models.TextField()
