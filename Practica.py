#%%Encabezado
# """

# """
#%%Importar modulos

# """

# """

#%%apartado 1

# print("hola mundo")

#%% apartado 2


# nombre = input("Nombre= ")
# edad = int(input("Edad= "))

# print("Te llamas", nombre , " y tienes", edad ,"años")

# if edad > 25:
#     print("Eres muy viejo")
# else:
#     print("Eres joven")
        
    
#%%apartado 3

# nombre = input("Nombre= ")
# if nombre.isdigit(): # Solo puedes ingresar letras
#     print("Error")
    
    
# try:
#     edad = int(input("Edad: ")) #solo puedes meter numeros
# except:
#     print("Mete un numero")
    
    
#%%apartado4
###############################################################################
                          #variables inmodificables
###############################################################################
#  """
#  int, str, tuplas, float, bool
#  """
# # #4.1 int
# # a = 10
# # b = 20
    
# # print(id(a), id(b))
# # #se alojan en el mismo espacio de memoria

# # print(a,b)


# #4.2 Str

# #4.3 Tuplas

# """
# LIsta que podemos crear pero no modificar
# """
# tupla  = (1, 2, 3)
# tupla = tupla + (4,)
# print(tupla)
# e2 = tupla[1] #empieza por 0
#a, b, c, d = tupla


# def calc_suma(a, b):
#     suma = a + b
#     resta = a - b
#     return suma, resta

# resultado = calc_suma(10, 5)
# print(type(resultado))




#4.4 Listas

# lista = [1,2,3,4]

# E0 = print(lista[0])

# lista_anidada = [1, 2, 3, [4, 5, [6, 7]]]

# n_filas1, n_columnas1 = 4, 2
# n_filas1, n_columnas1 = 2, 2
# n_filas1, n_columnas1 = 4, 3
# # M = []
# c = n_columnas1

# for i in range(n_filas1):
#     filas1 = []
#     for j in range(n_columnas1):
#         filas1.append(c)
#         c += 1
#     M.append(filas1)

# Forma bonita 
# M = [[0 for in range(n_columnas1)] 
#      for in range(n_filas1)  ]

# Matriz_numpy = np.arange(1, n_filas1 * n_columnas1 + 1)
# Matriz_numpy = np.reshape(Matriz_numpy, (n_filas1, n_columnas1))

# diccionario = {"nombre": "javier", "edad": 19}
# diccionario2 = {"nombre": "javier", "cursos": ["ESO", "SMR"]}

# empleados = {
#     "empleado 1" : {"nombre" : "Ivan", "nota" : 5},
#     "empleado 2" : {"nombre" : "Javier", "nota" : 6}
#     }

# print(empleados["empleado 1"]["nota"])



#conjuntos
# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}

# interseccion = conjunto1.intersection(conjunto2)


# booleano = 5 > 3

# fecha_entrega = int(input("Fecha entrega= "))
# coste = int(input("Coste= "))

# if fecha_entrega < 2 and coste > 100:
#     print("Urgente")
# if fecha_entrega == 2 and coste > 100:
#     print("Prioridad Media")
# if fecha_entrega > 2 and coste > 100 or coste < 100:
#     print("almacenado")
    
# colores = ["rojo", "amarillo", "rojo", "verde", "rojo"]
# color = "rojo"

# c = colores.count(color)

# print(f"El color {color} está en la lista {colores}, {c} veces")


# diccionario = {
#     "Sebastian": 19,
#     "danieZ": 21,
#     "Javier": 19,
#     "Manu": 26,
#     "Ana": 29
# }

# # Lista para almacenar los nombres de los mayores de edad
# mayores_de_edad = []

# for nombre, edad in diccionario.items():
#     if edad > 18:
#         mayores_de_edad.append(nombre)

# # Imprimir los resultados
# if mayores_de_edad:
#     print("Las siguientes personas son mayores de edad:")
#     for nombre in mayores_de_edad:
#         print(nombre)
# else:
#     print("No hay personas mayores de edad.")



# def saludar (nombre = None):
#     if nombre is None:
#         nombre = 'amigo'
#     print( f"Hola {nombre}" )

# saludar()











###############################################################################
                          #variables modificables
###############################################################################
















# Herencia y Polimorfismo


class animal:
    def __init__(self,nombre):
        self.name = nombre

    def hablar (self):
        return f"{self.name} hace x sonido"
    
class perro(animal):
    def hablar(self):
        return f"{self.name} hece guau"
    
    def raza(self,raza):
        self.raza = raza




















#♥




