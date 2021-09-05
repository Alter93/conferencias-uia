from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from presentaciones.models import Conferencia

from presentaciones.presentacion_util import ConferenciaZoom

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def en_vivo(request):
    fecha = timezone.now()
    conferencias = Conferencia.objects.filter(
        fecha_hora__lte=fecha
    ).order_by('lugar')
    
    conferencias_filtradas = []
    for conferencia in conferencias:
        if (conferencia.fecha_hora + conferencia.duracion > fecha):
            conferencias_filtradas.append(conferencia)
    if len(list(conferencias_filtradas)) == 0:
        texto_en_vivo = " - "
    else:
        conferencia = conferencias_filtradas[0]
        if conferencia.lugar == "0":
            texto_en_vivo = "Aula Magna - " + conferencia.titulo
        else:
            texto_en_vivo = "Sala " + conferencia.lugar + " - " + conferencia.titulo
    return HttpResponse(texto_en_vivo)

def horarios(request):
    if request.user.is_authenticated:
        return render(request, 'horarios.html', {})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def ponentes(request):
    if request.user.is_authenticated:
        return render(request, 'ponentes.html', {})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def conferencia(request, conf_uid):
    if request.user.is_authenticated:
        zoom = ConferenciaZoom(conf = conf_uid)
        print(zoom.conferencia.titulo)
        return render(request, 'conferencia/meeting.html', {
            'signature': zoom.signature,
            'apiKey': ConferenciaZoom.API_KEY,
            'meetingNumber': zoom.conferencia.zoom_id,
            'userName': 'Alejandro',
            'userEmail': 'aaaa@gmail.com',
            'passWord': zoom.conferencia.password_zoom,
            'redirect': request.path
        })
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def visitar_sala(request, id_sala):
    if request.user.is_authenticated:
        conferencia = ConferenciaZoom(lugar = id_sala).conferencia
        return render(request, 'sala.html', {
            'conf': conferencia,
            'lugar': id_sala,
        })
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
