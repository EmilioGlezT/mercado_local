from . import views
from django.urls import path
from productos_app.views import Catalogo_ListView, DetalleProductoView, ProductosListView

app_name = "productos_app"
urlpatterns = [
    path('', Catalogo_ListView.as_view(), name="inicio"),
    path("<int:pk>", DetalleProductoView.as_view(), name="detalle_producto"),
    path("listadoMisProductos/", ProductosListView.as_view(), name="list_mis_productos")
    
]