from . import views
from django.urls import path
from productos_app.views import Catalogo_ListView, DetalleProductoView

app_name = "productos_app"
urlpatterns = [
    path('', Catalogo_ListView.as_view(), name="inicio"),
    path("<int:pk>/", DetalleProductoView.as_view(), name="detalle_producto"),
]