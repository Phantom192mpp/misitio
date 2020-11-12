from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre   =models.TextField(max_length=50)
    direccion   =models.TextField(max_length=50)
    telefono   =models.TextField(max_length=50)
    encargado   =models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.TextField(max_length= 50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre   

class Categoria(models.Model):
    nombre   =models.TextField(max_length=50)
    activo   =models.BooleanField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo      = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion = models.TextField()
    stock       = models.IntegerField()
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    marca       = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    categoria   = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    run                = models.TextField(max_length=12)
    nombre             = models.TextField()
    email              = models.TextField()
    fechaNacimiento    = models.DateField()
    telefono           = models.TextField()
    region             = models.TextField()
    comuna             = models.TextField()
    nivelEducacional   = models.TextField()
    password           = models.TextField(max_length=50)
    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    folio          = models.TextField()
    fecha          = models.DateField()
    email          = models.EmailField(max_length=400)
    totalCompra    = models.IntegerField()
    producto       = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.SET_NULL)
    cliente        = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)
    sucursal       = models.ForeignKey(Sucursal, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.folio

class Detalle_Boleta(models.Model):
    idProducto        = models.TextField()
    idBoleta          = models.IntegerField()
    cantidad          = models.IntegerField()
    precioVenta       = models.IntegerField()
    subtotal          = models.IntegerField()
    boleta            = models.ForeignKey(Boleta, blank=True, null=True, on_delete=models.SET_NULL)



