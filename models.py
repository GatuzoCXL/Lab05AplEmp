from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
# Create your models here.
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
    
    #modelo cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    