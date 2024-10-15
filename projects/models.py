from django.db import models

IMAGE_COUNT = 10


def project_image_directory(instance, filename):
    return f"project_images/{instance.shortname}/{filename}"


class Project(models.Model):
    CATEGORIES = [
        ("web", "Web Design"),
        ("mobile", "Mobile"),
        ("wordpress", "Wordpress"),
        ("ecommerce", "E-commerce"),
    ]
    title = models.CharField(max_length=100)
    shortname = models.CharField(
        max_length=50,
        help_text="URL short name for the project, lowercase, hyphenated. Also serves as name for media folder.",
        primary_key=True,
    )
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES, default="web")
    client = models.CharField(max_length=100)
    date = models.DateField(max_length=20)
    link_text = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    coverimage = models.FileField("Cover Image", upload_to="project_images/", blank=True)


# Add image fields to the Project model
for i in range(1, IMAGE_COUNT + 1):
    Project.add_to_class(
        "image%s" % i,
        models.FileField(f"Image {i}", upload_to=project_image_directory, blank=True),
    )
