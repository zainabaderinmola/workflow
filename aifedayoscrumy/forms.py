from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.models import User,Group
from .models import *
from django import forms

class SignUpForm(ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password',)
		widgets = {
			'first_name' : TextInput(attrs ={'class': 'form-control'}),
			'last_name' : TextInput(attrs ={'class': 'form-control'}),
			'email' : TextInput(attrs ={'class': 'form-control'}),
			'username' : TextInput(attrs ={'class': 'form-control'}),
			'password' : TextInput(attrs ={'class': 'form-control'}),
		}

class CreateGoalForm(ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['goal_name', 'user', 'goal_status']
		widgets = {
			'goal_name' : TextInput(attrs ={'class': 'form-control'}),
			'user' : Select(attrs ={'class': 'form-control'}),
			'goal_status' : Select(attrs ={'class': 'form-control'}),
		}

class MoveGoalForm(forms.ModelForm):
    
	class Meta:
		model = ScrumyGoals
		fields = ( 'goal_name', 'user', 'goal_status' )
		widgets = {
			'goal_name' : TextInput(attrs ={'class': 'form-control'}),
			'user' : Select(attrs ={'class': 'form-control'}),
			'goal_status' : Select(attrs ={'class': 'form-control'}),
		}