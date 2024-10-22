#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:14:01 2024

@author: ivan
"""
from abc import ABC, abstractmethod

class Empresa:
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados
    
    def agregarEmpleado(self, empleado1):
        if isinstance(empleado1, Empleado):    
            self.empleados.append(empleado1)
            print(f"Empleado {empleado1.nombre} agregado exitosamente.")
        else:
            print("El empleado no se ha podido agregar.")
    
    def mostrarInfo(self):
        print(f"\n{'=' * 40}")
        print(f"Nombre de la empresa: {self.nombre}")
        print(f"{'=' * 40}")
        self.calcularCosteEmpleados()
        print(f"{'=' * 40}")
    def calcularCosteEmpleados(self):
        Total = 0
        for empleado in self.empleados:
            print("--------------------------------------")
            empleado.mostrarInfo()
            print("--------------------------------------")
            Total += empleado.coste()
        return f"El coste total de todos los empleados al mes es {Total}€"
    
class Empleado(ABC):
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id 
        
    @abstractmethod
    def mostrarInfo(self):
        pass
    
    @abstractmethod
    def coste(self):
        pass

class Asalariado(Empleado):
    def __init__(self, nombre, edad, id, saldo):
        super().__init__(nombre, edad, id)  
        self.saldo = saldo

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}\n"
              f"Id: {self.id}\n"
              f"Saldo: {self.saldo}€")
    
    def coste(self):
        return self.saldo

class PorHora(Empleado):
    def __init__(self, nombre, edad, id, tarifaPorHora, horas):
        super().__init__(nombre, edad, id)  
        self.tarifaPorHora = tarifaPorHora
        self.horas = horas

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}\n"
              f"Id: {self.id}\n"
              f"Tarifa por hora: {self.tarifaPorHora}€\n"
              f"Horas: {self.horas}")
    
    def coste(self):
        return self.tarifaPorHora * self.horas
    
def crearEmpleado():
    print("\n" + "=" * 30)
    print("Crear nuevo empleado")
    print("=" * 30)
    
    nombre = input("Nombre: ")
    try:
        edad = float(input("Edad: "))
    except ValueError:
        edad = 0
        print("Edad no válida. Se establecerá en 0.")
        
    id = input("Id: ")
    
    while True:
        tipo = input("Tipo ('Asalariado', 'PorHora'): ").strip().lower()
        
        if tipo == "asalariado":
            while True:
                try:
                    salario = float(input("Salario: "))
                    print("Empleado creado.")
                    return Asalariado(nombre, edad, id, salario)
                except ValueError:
                    print("Salario incorrecto. Vuelve a intentar.")
            
        elif tipo == "porhora":
            while True:
                try:
                    tarifaPorHora = float(input("Tarifa por hora: "))
                    horas = float(input("Horas: "))
                    print("Empleado creado.")
                    return PorHora(nombre, edad, id, tarifaPorHora, horas)
                except ValueError:
                    print("Valor incorrecto. Intente de nuevo.")
        else:
            print("Tipo no válido. Intente de nuevo.")

def menu():
    print("\n" + "=" * 30)
    print("Menú de opciones")
    print("=" * 30)
    print("1. Crear empleado")
    print("2. Mostrar información de la empresa")
    print("3. Mostrar coste de los empleados")
    print("4. Salir")
    print("=" * 30)
    
if __name__ == '__main__':
    empresa = Empresa("Empresa1", [])
    while True:
        menu()
        opcion = input("Elige opción: ")
        match opcion:
            case "1":
                empresa.agregarEmpleado(crearEmpleado())
            case "2":
                empresa.mostrarInfo()
            case "3":
                print(empresa.calcularCosteEmpleados())
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
