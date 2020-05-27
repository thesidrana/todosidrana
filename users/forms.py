from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #Gives nested nameplace for configs
        model = User #Forms.save saves it to user model
        fields = ['username','email','password1', 'password2'] #Fields that should be shown on form

#A form that updates user models

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    address = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm)        :
    class Meta:
        model = Profile
        fields =['image']
