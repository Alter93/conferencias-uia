from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
