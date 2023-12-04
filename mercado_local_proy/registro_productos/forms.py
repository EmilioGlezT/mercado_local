from django import forms
from productos_app.models import Producto

class RegistroProducto(forms.ModelForm):
   class Meta:
        model = Producto
        fields = "__all__"
