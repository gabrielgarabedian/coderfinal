"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from AppCoder.views import mostrar_mi_template, saludo, saludo_dos, saludar
from ejemplo.views import  (index, index_dos, index_tres, imc, 
                            monstrar_familiares,BuscarFamiliar, 
                            AltaFamiliar)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/saludar', saludo),
    path('hola-mundo/saludo2', saludo_dos),
    path('hola-mundo/saludar/<nombre>', saludar),
    path('mostrar-mi-template/', mostrar_mi_template),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index_dos),
    path('mostrar-nota/', index_tres),
    path('mostrar-imc/<int:peso>/<int:altura>/', imc),
    path('mi-familia/', monstrar_familiares,),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('panel-familia/', include('panel_familia.urls')),
    path('blog/', include('blog.urls')),
    path('tienda/', include('tienda.urls')),
    path('rutina/', include('rutina.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)