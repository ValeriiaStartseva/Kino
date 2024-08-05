from django import forms
from django.forms.widgets import PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User


# create or register a user
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'password1', 'password2', 'address', 'num_card', 'language',
                  'gender', 'phone', 'date_birthday', 'city']


# authenticate a user
class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'address', 'num_card', 'language',
                  'gender', 'phone', 'date_birthday', 'city', 'is_staff', 'is_active']

        widgets = {
            'email': forms.EmailInput(),
        }
