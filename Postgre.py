#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:32:21 2024

@author: ivan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:04:50 2024

@author: ivan
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

def connect_bd(host,database,user,password,port):
    try:
        connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
        if connection.is_connected():
            print(f"La conexion ha sido exitosa {database}")
            return connection
    except Error as e:
            print(f"Error = {e}")
            return None
# Funcion para leer
def read_bd(connection,table,columns,limit_row):
    try:
        cursor = connection.cursor()
        #Peticion
        columns_str = ','.join(columns)
        query = f"SELECT {columns_str} FROM {table} LIMIT  {limit_row};"
        cursor.execute(query)
        #Resultados
        results = cursor.fetchall()
        #Obtener 
        columns_result = [i[0] for i in cursor.description]
        df = pd.DataFrame(results,columns=columns_result)
        return df
    except Error as e:
        print(f"The error is {e}")
        return None
if __name__ == '__main__':
    #Parametros
    host = 'mysql-rfam-public.ebi.ac.uk'
    database = 'Rfam'
    user = 'rfamro'
    password = ''
    port = 4497
    tabla = 'family'
    columnas = ['rfam_acc','rfam_id','description']
    limite_filas = 5
    # conectar 
    conexion = connect_bd(host, database, user, password, port)
    if conexion:        
        df_db =read_bd(conexion, tabla,columnas, limite_filas)
        if df_db is not None:
            print(df_db)
            conexion.close()