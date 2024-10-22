#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:02:22 2024

@author: ivan
"""


from pymongo.mongo_client import MongoClient
import pandas as pd

uri = "mongodb+srv://DB:1234@cluster0.xf3xr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Conectado correctamen")
    
    
except Exception as e:
    print(e)
    exit(1)
    
# =============================================================================
# extraer info
# =============================================================================
db = client["sample_mflix"]
coleccion = db["movies"]
try:
    resultados = coleccion.find().limit(10)
    lista_resultados = list(resultados)
    if not lista_resultados :
        print("Error")
    else:
        print(f"Se han encontrado {len(lista_resultados)} documentos")
except Exception() as e:
    print(e)
df = pd.DataFrame(lista_resultados)
print(df)