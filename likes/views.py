from django.shortcuts import render, redirect
from likes.models import Cartel
from likes.models import Like
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def registrar_like(request, id_cartel):
    # Seleccionar por id_usuario.
    # Si no existe, generar registro con id_cartel.
    # Si ya existe, cambiar id_cartel en el registro.
    if request.user.is_authenticated:
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
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def cargar_carteles(request):
    if request.user.is_authenticated:
        carteles = Cartel.objects.all()
        html = []
        for cartel in carteles:
            html.append(cartel.generar_cartel(request.user.id))

        return render( request, 'expo.html', {'carteles': html })
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
