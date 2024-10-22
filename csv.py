#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:51:06 2024

@author: ivan
"""

import pandas as pd

# Leer el archivo CSV
archivo = pd.read_csv("csv.csv")

# Columnas
nombres = archivo['nombre']

# Filas
fila1 = archivo.loc[0]

# Acceder a valor en concreto
Salario3 = archivo.loc[2, 'salario_mensual']

print(fila1)
print("El salario del empleado 3: ", Salario3)
print(f"Los datos de los empleados son:\n{nombres}")

# Crear nueva fila
nuevaFila = {
    'nombre': 'Javier',
    'edad': 19,
    'id_empleado': '4',
    'horas_trabajadas': 120,
    'tarifa_hora': 5,
    'salario_mensual': 1200
}

# Añadir nueva fila al DataFrame
archivo = pd.concat([archivo,pd.DataFrame([nuevaFila])])

# Guardar los cambios en un nuevo archivo CSV (opcional)
archivo.to_csv("csv_actualizado.csv", index=False)
