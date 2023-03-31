from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AddprojectModel

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=65, widget=forms.EmailInput)
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']
