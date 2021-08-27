from django.db import models

# Create your models here.

class Prerregistro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    comunidad = models.CharField(max_length=100)
    cantidad_pagada = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "prerregistro"
