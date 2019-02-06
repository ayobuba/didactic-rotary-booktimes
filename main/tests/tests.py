from django.test import TestCase
from django.urls import reverse

from main import forms
# Create your tests here.


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        # self.assertContains(response,'booktimes')


    def test_about_page_works(self):
        response = self.client.get(reverse("about-us"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"about-us.html")
        # self.assertContains(response,'booktimes')


    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,template_name="main/contact-us.html")
        self.assertIsInstance(response.context["form"], forms.ContactForm)
