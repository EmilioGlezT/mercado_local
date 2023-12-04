from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mercado_local_app.models import UserProfile, AbstractUser


class RegisterForm(forms.ModelForm):
   class Meta:
        model = UserProfile
        fields = "__all__"

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class RegisterVendedorForm(forms.ModelForm):
#     class Meta:
#         model = Vendedor
#         fields = "__all__"

# class RegisterClienteForm(forms.ModelForm):
#     class Meta:
#         model= Cliente
#         fields = "__all__"