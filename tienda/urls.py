from django.urls import path
from tienda.views import *

urlpatterns = [
     path('', index, name="index-tienda"),

     ]