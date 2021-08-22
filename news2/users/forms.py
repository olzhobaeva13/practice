from django import forms
from django.forms import widgets

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# class RegistrationForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.TextInput())