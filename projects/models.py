from django.db import models


def project_image_directory(instance, filename):
    return f"project_images/{instance.shortname}/{filename}"


class Project(models.Model):
    CATEGORIES = [("web", "Web Design"), ("mobile", "Mobile"), ("wordpress", "Wordpress"), ("ecommerce", "E-commerce")]
    title = models.CharField(max_length=100)
    shortname = models.CharField(
        max_length=50,
        help_text="Short name for the project, lowercase, hyphenated. Also serves as name for media folder.",
    )
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES, default="web")
    client = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    url = models.URLField(blank=True)
    coverimage = models.FileField("Cover Image", upload_to="project_images/", blank=True)
    image1 = models.FileField("Image 1", upload_to=project_image_directory, blank=True)
    image2 = models.FileField("Image 2", upload_to=project_image_directory, blank=True)
    image3 = models.FileField("Image 3", upload_to=project_image_directory, blank=True)
    image4 = models.FileField("Image 4", upload_to=project_image_directory, blank=True)
    image5 = models.FileField("Image 5", upload_to=project_image_directory, blank=True)
