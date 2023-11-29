from . import views
from django.urls import path
from compra_app.views import ver_carrito, agregar_al_carrito

app_name = "compra_app"
urlpatterns = [
     path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
     path('carrito/', ver_carrito, name='ver_carrito'),
    ##path('carrito/', Carrito_ListView.as_view(), name='carrito'),
]