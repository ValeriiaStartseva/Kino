from django import forms
from .models import EmailCampaign


class EmailCampaignForm(forms.ModelForm):
    ALL_USERS = 'all'
    SELECTED_USERS = 'selected'
    USER_CHOICES = [
        (ALL_USERS, 'Всі користувачі'),
        (SELECTED_USERS, 'Вибрати користувачів'),
    ]

    users = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect)
    html_file = forms.FileField(label='Завантажити HTML-лист', required=False)

    class Meta:
        model = EmailCampaign
        fields = ['users', 'html_file']
