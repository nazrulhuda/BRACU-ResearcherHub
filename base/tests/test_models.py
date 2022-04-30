from django.test import TestCase 
from base.models import *

class ModelsTest(TestCase):
    def TestTopic(self):   
        self.topic1 = Topic.objects.create(name='machine learning')
        
    def test_Topic_is_assignedcreation(self):
        self.assertEquals(self.topic1, 'Machine Learning')