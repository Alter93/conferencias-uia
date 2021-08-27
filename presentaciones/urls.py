from django.urls import path
from presentaciones import views

urlpatterns = [
    path('', views.home, name='home'),
]
