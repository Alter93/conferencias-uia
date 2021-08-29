import pandas as pd

from django.shortcuts import render

from prerregistro.models import Prerregistro

# Create your views here.
def cargar_usuarios(request):

    df = pd.read_csv("prerregistro/reporte_psicologia.csv")


    for i,row in df.iterrows():
        try:
            registro = Prerregistro(
                nombre = row['nombre'],
                apellido = row['apellido'],
                email = row['email'],
                comunidad = row['comunidad'],
                cantidad_pagada = row['cantidad_pagada']
            )

            registro.save()
        except Exception as e:
            print(e)
