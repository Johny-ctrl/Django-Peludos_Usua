from django.db import models


# Create your models here.

#Modeo Categoria
class Categoria(models.Model):
    idCategoria = models.CharField(max_length= 5 , primary_key=True, verbose_name='Id categoria')
    NombreCategoria = models.CharField(max_length= 35 , verbose_name='Nombre Categoria')
    def __str__(self):
        return self.NombreCategoria

#Modelo de productos
class Producto(models.Model):
    id = models.CharField(max_length= 5 ,primary_key=True, verbose_name='id producto')
    nombre = models.CharField(max_length= 20 , verbose_name='Nombre productos')
    descripcion = models.TextField(max_length=100 , verbose_name='Descripcion de producto')
    precio = models.IntegerField(verbose_name='Precio producto')
    imagen = models.ImageField(null = True, upload_to ="Productos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
