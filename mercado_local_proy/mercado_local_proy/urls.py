"""
URL configuration for mercado_local_proy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from mercado_local_app import views
import mercado_local_app.views
urlpatterns = [
    path('', mercado_local_app.views.pagina_inicio, name= 'pagina_inicio'),
    path('admin/', admin.site.urls),
    path('login', mercado_local_app.views.login_view, name='login'),
    path('register', mercado_local_app.views.register_view, name='register'),
    path('crear-producto', mercado_local_app.views.crear_producto, name='crear-producto')
]
