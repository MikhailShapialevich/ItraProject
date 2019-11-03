from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shirt
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreateShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = ('picture_of_shirt', 'name_of_shirt', 'description_of_shirt', 'user', 'topic')

