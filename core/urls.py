from django.urls import path
from .views import home, Productos, AgregarCat, AgregarPro,Registro

urlpatterns = [
    path('', home, name='home'),
    path('Productos',Productos, name='Productos'),
    path('AgregarProducto', AgregarPro, name= 'AgregarPro'),
    path('AgregarCat', AgregarCat, name='AgregarCat'),
    path('Registro', Registro, name="Registro")
]