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

def conferencia(request, conf_uid):
    zoom = ConferenciaZoom(conf = conf_uid)
    print(zoom.conferencia.titulo)
    return render(request, 'conferencia/meeting.html', {
        'signature': zoom.signature,
        'apiKey': ConferenciaZoom.API_KEY,
        'meetingNumber': zoom.conferencia.zoom_id,
        'userName': 'Alejandro',
        'userEmail': 'alexae93@gmail.com',
        'passWord': zoom.conferencia.password_zoom
    })

def lista_conferencias(request):
    return render(request, 'conferencia/lista_conferencias.html', {
        'conf_0': ConferenciaZoom(lugar = '0').conferencia,
        'conf_1': ConferenciaZoom(lugar = '1').conferencia,
        'conf_2': ConferenciaZoom(lugar = '2').conferencia,
        'conf_3': ConferenciaZoom(lugar = '3').conferencia,
        'conf_4': ConferenciaZoom(lugar = '4').conferencia,
        'conf_5': ConferenciaZoom(lugar = '5').conferencia,
    })
