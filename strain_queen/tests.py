from django.test import TestCase
from django.http import response
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import unittest

# Create your tests here.
class TestStuff(TestCase):
    # Status
    def test_main_page_status(self):
        url = reverse('strain_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_page_status(self):
        url = reverse('strain_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Templates
    def test_list_page_template(self):
        url = reverse('strain_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'strain_list.html')

    def test_create_page_template(self):
        url = reverse('strain_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'strain_create.html')

    def test_base_template(self):
        url = reverse('strain_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
