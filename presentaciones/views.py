from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

from presentaciones.presentacion_util import ConferenciaZoom

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def horarios(request):
    if request.user.is_authenticated:
        return render(request, 'horarios.html', {})
    else:
        return render(request, 'horarios.html', {})
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def ponentes(request):
    if request.user.is_authenticated:
        return render(request, 'ponentes.html', {})
    else:
        return render(request, 'ponentes.html', {})
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def conferencia(request, conf_uid):
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

def visitar_sala(request, id_sala):
    conferencia = ConferenciaZoom(lugar = id_sala).conferencia
    return render(request, 'sala.html', {
        'conf': conferencia,
        'lugar': id_sala,
    })
