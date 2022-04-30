from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *


        
class UrlsTest(SimpleTestCase): 
    
    def test_home_url_resolves(self):
        url = reverse('home') 
        self.assertEquals(resolve(url).func, home) 
        
    def test_login_url_resolves(self): 
        url = reverse('login') 
        self.assertEquals(resolve(url).func, loginPage)
        
    def test_create_room_url_resolves(self):
        url = reverse('create-room') 
        self.assertEquals(resolve(url).func, createRoom) 
        
    def test_update_use_url_resolves(self): 
        url = reverse('update-user') 
        self.assertEquals(resolve(url).func, updateUser) 
        
    def test_add_topic_url_resolves(self): 
        url = reverse('topics') 
        self.assertEquals(resolve(url).func, topicsPage) 
        
    def test_roomdetail_url_resolves(self): 
        url = reverse('room', args=['someslug'])
        self.assertEquals(resolve(url).func, room) 
        
    def test_profiledetail_url_resolves(self): 
        url = reverse('user-profile', args=['someslug'])
        self.assertEquals(resolve(url).func, userProfile) 