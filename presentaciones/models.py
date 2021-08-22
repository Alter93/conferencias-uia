from django.db import models

# Create your models here.
class Conferencista(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    
class Conferencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    fecha_hora = models.DateTimeField()
    duracion = models.DecimalField(max_digits=3, decimal_places=2)
    lugar = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    id_conferencista = models.ForeignKey('Conferencista', on_delete=models.CASCADE)
    uuid = models.CharField(max_length=64)
    

