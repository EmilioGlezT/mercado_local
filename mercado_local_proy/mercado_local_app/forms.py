from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    location = forms.CharField(max_length=50, required=False, help_text='Optional.')
    bio = forms.CharField(max_length=400, required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('location', 'bio')