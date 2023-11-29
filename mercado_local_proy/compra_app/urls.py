from . import views
from django.urls import path
from compra_app.views import Carrito_ListView

app_name = "compra_app"
urlpatterns = [
    path('carrito/', Carrito_ListView.as_view(), name='carrito'),
]