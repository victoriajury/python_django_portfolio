from django.test import Client, TestCase
from django.urls import reverse
from projects.models import Project


class ProjectTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.project1 = Project.objects.create(
            title="Some Project Title",
            shortname="some-project-title",
            description="A brief description of this project.",
            category="web",
            client="Some Company",
            date="2020-03-01",
            link_text="www.company-website.com",
            url="https://company-website.com",
            coverimage="project_images/some-project-title/cover-image.jpg",
        )
        cls.project2 = Project.objects.create(
            title="Some Other Project Title",
            shortname="some-other-project-title",
            description="A brief description of this project.",
            category="wordpress",
            client="Some Other Company",
            date="2017-04-01",
            link_text="www.other-company-website.com",
            url="https://other-company-website.com",
            coverimage="project_images/some-other-project-title/cover-image.jpg",
        )

    def test_projects_created(self):
        self.assertEqual(self.project1.title, "Some Project Title")
        self.assertEqual(self.project1.category, "web")
        self.assertEqual(self.project1.url, "https://company-website.com")

        self.assertEqual(self.project2.title, "Some Other Project Title")
        self.assertEqual(self.project2.category, "wordpress")
        self.assertEqual(self.project2.url, "https://other-company-website.com")


class ProjectDetailViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.project = Project.objects.create(
            title="Some Project Title",
            shortname="some-project-title",
            description="A brief description of this project.",
            category="wordpress",
            client="Some Company",
            date="2020-03-01",
            link_text="www.company-website.com",
            url="https://company-website.com",
            coverimage="project_images/some-project-title/cover-image.jpg",
        )

    def test_project_index_view(self):
        self.url = reverse("project_index")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_index.html")
        self.assertContains(response, "Some Project Title")
        self.assertContains(response, "Wordpress", 2)  # Count=2 as one is category button

    def test_project_detail_view(self):
        self.url = "/projects/some-project-title/"
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_detail.html")
        self.assertContains(response, "Some Project Title")
        self.assertContains(response, "A brief description of this project.")
        self.assertContains(response, "Wordpress", 1)
