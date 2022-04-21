from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']

class DashboardFom(forms.Form):
      text= forms.CharField(max_length=100,label="Enter the topics that interests you      ")
