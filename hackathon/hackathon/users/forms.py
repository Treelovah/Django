from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    additional fields for registration form, if needed
    """
    # email = forms.EmailField()

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    
    
    class Meta:
        model = User
        fields = ['username'] # need to add email at somepoint


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

