from django import forms
from django.forms.widgets import PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User
from django.contrib.auth import authenticate


# create or register a user on site
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'password1', 'password2', 'address', 'num_card', 'language',
                  'gender', 'phone', 'date_birthday', 'city']


# authenticate a user on site
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


class UserProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'address', 'num_card', 'phone', 'language', 'gender',
                  'date_birthday', 'city']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'num_card': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
        return cleaned_data


class AdminAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_superuser:
            raise forms.ValidationError(
                "This user does not have access to admin",
                code='no_access'
            )


