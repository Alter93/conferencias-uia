from django.urls import path
from presentaciones import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('conferencia/lista', views.lista_conferencias, name='lista'),
    path('conferencia/<uuid:conf_uid>', views.conferencia, name='conferencia'),
    path('horarios', views.horarios, name='horarios'),
    path('ponentes', views.ponentes, name='ponentes'),
]
