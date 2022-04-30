from django.test import TestCase, Client
from django.urls import reverse
from base.models import *
import json

class ViewsTest(TestCase):
    def test_room_list_GET(self):
        client = Client()
        response = client.get(reverse('home')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html') 
        
    def test_topic_list_GET(self):
        client = Client()
        response = client.get(reverse('topics')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/topics.html') 
        
    def test_topic_list_GET(self):
        client = Client()
        response = client.get(reverse('user-profile')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/profile.html') 