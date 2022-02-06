import pandas as pd

from django.shortcuts import render

from prerregistro.models import Prerregistro

# Create your views here.
def cargar_usuarios(request):

    df = pd.read_csv("prerregistro/lista_usuarios.csv")


    for i,row in df.iterrows():
        try:
            registro = Prerregistro(
                nombre = row['NOMBRE'],
                apellido = "NA",
                email = row['CORREO'],
                comunidad = "NA",
                cantidad_pagada = 1.0
            )

            registro.save()
        except Exception as e:
            print(e)
