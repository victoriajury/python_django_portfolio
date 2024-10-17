from profile.models import ResumeEducation, ResumeExperience, ResumeSkill, ResumeSummary

from django.test import TestCase


class ResumeSummaryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = ResumeSummary.objects.create(
            name="Joan Smith",
            bio="A few words about me.",
            address="Anywhere, Anytown, AB12 3CD",
            telephone="01235 456 789",
            email="someone@example.com",
        )

    def test_user_created(self):
        self.assertEqual(self.user.name, "Joan Smith")
        self.assertEqual(self.user.bio, "A few words about me.")
        self.assertEqual(self.user.email, "someone@example.com")


class ResumeEducationTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.edu1 = ResumeEducation.objects.create(
            location="Some school1",
            date_attended="2010 - 2012",
            study_details="Certificates, exams, degrees",
            position=1,
        )
        cls.edu2 = ResumeEducation.objects.create(
            location="Some school2",
            date_attended="2013 - 2018",
            study_details="Certificates, exams, degrees",
            position=2,
        )

    def test_education_created(self):
        self.assertEqual(self.edu1.location, "Some school1")
        self.assertEqual(self.edu2.date_attended, "2013 - 2018")
        self.assertEqual(self.edu2.study_details, "Certificates, exams, degrees")


class ResumeSkillTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.skill1 = ResumeSkill.objects.create(category="Technical skills", skill="Python", position=1)
        cls.skill2 = ResumeSkill.objects.create(category="Languages", skill="French", position=2)

    def test_skill_created(self):
        self.assertEqual(self.skill1.skill, "Python")
        self.assertEqual(self.skill2.category, "Languages")
        self.assertEqual(self.skill2.skill, "French")


class ResumeExperienceTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.exp1 = ResumeExperience.objects.create(
            role="Software Engineer",
            date_attended="2020 - 2021",
            location="Some Company Ltd",
            role_details="Testing, developing software, REST APIs",
            position=1,
        )
        cls.exp2 = ResumeExperience.objects.create(
            role="Website Developer",
            date_attended="2021 - 2024",
            location="Another Enterprise Ltd",
            role_details="Testing, developing software, REST APIs",
            position=2,
        )

    def test_experience_created(self):
        self.assertEqual(self.exp1.location, "Some Company Ltd")
        self.assertEqual(self.exp2.date_attended, "2021 - 2024")
        self.assertEqual(self.exp2.role_details, "Testing, developing software, REST APIs")
