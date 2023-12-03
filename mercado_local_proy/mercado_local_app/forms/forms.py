from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from mercado_local_app.models import CustomUser, Vendedor, Cliente


class RegisterForm(forms.ModelForm):
   class Meta:
        model = CustomUser
        fields = "__all__"


class RegisterVendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = "__all__"

class RegisterClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = "__all__"