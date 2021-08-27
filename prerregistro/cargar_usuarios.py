import pandas as pd
import mysql.connector
#from django.contrib.auth.models import User


def cargar_usuarios():
    connection = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='conferenciasuia')

    cursor = connection.cursor()

    df = pd.read_csv("reporte_psicologia.csv")

    cols = "`,`".join([str(i) for i in df.columns.tolist()])

    for i,row in df.iterrows():
        sql = "INSERT INTO `prerregistro` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        try:
            cursor.execute(sql, tuple(row))
            print("Fila insertada")
        except mysql.connector.errors.IntegrityError as error:
            print(error)
            # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        # the connection is not autocommitted by default, so we must commit to save our changes
        connection.commit()

cargar_usuarios()
