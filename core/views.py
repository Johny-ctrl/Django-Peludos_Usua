from django.shortcuts import render
from core.form import FormularioPro, FormularioCat,CreacionDeUsuario,Login
from .models import Producto,Categoria
from rest_AmigosP.viewslogin import login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.

def home(request):

    return render(request, 'core/index.html')

def Productos(request):
     #Se define objeto para obtener los productos
    #Se puede utilizar Producto.object.all() o 'select * from Producto'
    productos = Producto.objects.all()

    #Se cargan los objetos obtenidos en la variable
    contexto = {
        'productos' : productos
    }
    return render(request, 'core/Productos.html', contexto)

#Agregar Productos
def AgregarPro(request):
    
    contexto ={
        'producto' : FormularioPro()
    }

    #Se verifican los datos de producto
    if request.method == 'POST':
        #S recuperan los datos
        producto = FormularioPro(request.POST, request.FILES)
        #validacion de formulario
        if producto.is_valid:
            producto.save()
            contexto['mensaje'] = "Creado correctamente"
    return render(request, 'core/agregarPro.html', contexto)

#Agregar una categoria
def AgregarCat(request):
    contexto ={
        'categoria': FormularioCat()
    }

        #Se verifican los datos de categoeia
    if request.method == 'POST':
        #S recuperan los datos
        categoria = FormularioCat(request.POST)
        #validacion de formulario
        if categoria.is_valid:
            categoria.save()
            contexto['mensaje'] = "Creado correctamente"
    return render(request, 'core/agregarCat.html', contexto)

#para el registro de usuario
def Registro(request):
    data = {
        'form': CreacionDeUsuario()
    }
    if request.method ==  'POST':
        formulario = CreacionDeUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro completado con exito")
            #redireccion
            return redirect(to='iniSesion')
        data["form"] = formulario
    return render(request , 'core/Registro.html', data)