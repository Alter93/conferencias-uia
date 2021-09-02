from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

from presentaciones.presentacion_util import ConferenciaZoom

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

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
