from . import views
from django.urls import path
from compra_app.views import ver_carrito, agregar_al_carrito, eliminar_del_carrito, modificar_cantidad_carrito

app_name = "compra_app"
urlpatterns = [
     path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
     path('carrito/', ver_carrito, name='ver_carrito'),
     path('eliminar_del_carrito/<int:orden_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
     path('modificar_cantidad_carrito/<int:orden_id>/<str:operacion>/', modificar_cantidad_carrito, name='modificar_cantidad_carrito'),
    ##path('carrito/', Carrito_ListView.as_view(), name='carrito'),
]