from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    url = models.URLField(blank=True)