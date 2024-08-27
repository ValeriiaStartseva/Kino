from django import forms
from django.forms.widgets import PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User
from django.contrib.auth import authenticate

# create or register a user
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'password1', 'password2', 'address', 'num_card', 'language',
                  'gender', 'phone', 'date_birthday', 'city']


# authenticate a user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user = authenticate(email=email, password=password)
            if not self.user:
                raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data

    def get_user(self):
        return self.user


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'address', 'num_card', 'language',
                  'gender', 'phone', 'date_birthday', 'city', 'is_staff', 'is_active']

        widgets = {
            'email': forms.EmailInput(),
        }
