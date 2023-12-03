from .views import crearProduto,createProducto, saveProducto
from django.urls import path
from productos_app.views import Catalogo_ListView, DetalleProductoView

app_name = "producto"
urlpatterns = [
    path('create/' , createProducto, name = "create"),
    path('crear/', crearProduto),
    path('save/', saveProducto, name= 'save')
]