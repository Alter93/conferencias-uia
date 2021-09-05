from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# Create your models here.
class Cartel(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=500)
    categoria = models.CharField(max_length=200)
    imagen = models.CharField(max_length=2000)
    dia = models.CharField(max_length=2)
    sala = models.CharField(max_length=2)

    def generar_cartel(self,id_usuario):

        numero = len(list(Like.objects.filter(cartel=self.id)))
        usuario = User.objects.get(
            id = id_usuario
        )
        gracias = None
        try:
            like = Like.objects.get(
                usuario = usuario,
                cartel = self
            )
            gracias = "Gracias por tu voto."

        except Like.DoesNotExist as e:
            gracias = None

        html = render_to_string("cartel.html",{
            "id": self.id,
            "titulo": self.titulo,
            "imagen": self.imagen,
            "numero": numero,
            "categoria": self.categoria,
            "url_voto": f"/likes/registrar/{self.id}",
            "voto":gracias
        })
        return html

class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    cartel = models.ForeignKey(Cartel, on_delete=models.CASCADE, null=True)
