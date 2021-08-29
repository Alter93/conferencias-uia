from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Prerregistro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    comunidad = models.CharField(max_length=100)
    cantidad_pagada = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    usuario_db = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    def save(self, *args, **kwargs):
        usuario = User.objects.create_user(slugify(self.nombre + "-" + self.apellido) , self.email, 'W3lcome2!')
        success = True
        try:
            usuario.save()

        except Exception e:
            success = False

        if success:
            self.usuario_db = usuario
            super().save(*args, **kwargs)

    class Meta:
        db_table = "prerregistro"
