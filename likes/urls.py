from django.urls import path
from likes import views

urlpatterns = [
    path('likes/registrar/<int:id_user>/<int:id_cartel>', views.registrar_like, name='registrar'),
    path('expo', views.cargar_carteles, name='cargar'),

]
