from django.shortcuts import render, redirect
from likes.models import Cartel
from likes.models import Like
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def registrar_like(request, id_user, id_cartel):
    # Seleccionar por id_usuario.
    # Si no existe, generar registro con id_cartel.
    # Si ya existe, cambiar id_cartel en el registro.
    cartel = Cartel.objects.get(
        id = id_cartel
    )
    usuario = User.objects.get(
        id = request.user.id
    )

    try:
        like = Like.objects.get(
            usuario = usuario
        )
        like.cartel = cartel
    except Like.DoesNotExist as e:
        like = Like(cartel = cartel, usuario = usuario)
    like.save()

    return redirect('/expo')


def cargar_carteles(request):
    carteles = Cartel.objects.all()
    html = []
    for cartel in carteles:
        html.append(cartel.generar_cartel(request.user.id))

    return render( request, 'registration/expoWIP.html', {'carteles': html })
