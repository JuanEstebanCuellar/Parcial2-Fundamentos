# Parcial 2 (Fundamentos de programación)
# Integrantes: Christopher Villa Noreña - Juan Esteban Cuellar Trujillo -  Juan José Vallejo Muñoz
# Fecha: 12  de octubre del 2023


import random

def Saludo ():
    print("Hola, bienvenido a este programa")
    print("************************************************************************************************")
    print("En este programa vamos a observar la realizacion del parcial de Fundamentos de la Programacion.")
    print("************************************************************************************************")


def Vector_1():
    return [random.randint(0, 20) for i in range(0, 50)]

def Vector_Repet(Vectores):
    return list(set(Vectores))

def Cantidad_Repet(Vectores, num):
    return Vectores.count(num)

# A. Generar una matriz 5x5 con números aleatorios entre 100 y 200.
def Primer_Matriz():
    matriz = [[random.randint(100, 200) for _ in range(5)] for _ in range(5)]
    return matriz

# B. Crear una segunda matriz siguiendo las reglas dadas.
def Segunda_Matriz(matriz):
    matriz_dos = []
    for columna in range(5):
        fila_dos = []
        for fila in range(5):
            if columna == 0:
                fila_dos.append(matriz[fila][columna] ** 2)
            else:
                fila_dos.append(matriz[fila][columna] ** 4)
        matriz_dos.append(fila_dos)
    return matriz_dos


def SumarCada_Fila(matriz):
    return [sum(fila) for fila in matriz]

def SumarCada_Columna(matriz):
    return [sum(fila[x] for fila in matriz) for x in range(5)]

def Resta_Matrices(Matriz_1, Matriz_2):
    return [[Matriz_2[x][y] - Matriz_1[x][y] for y in range(5)] for x in range(5)]

def Multiplicar_Matriz_Numero(matriz, Numero):
    return [[Numero * matriz[x][y] for y in range(5)] for x in range(5)]

def Multiplicar_Matrices(Matriz_1, Matriz_2):
    return [[sum(Matriz_1[x][z] * Matriz_2[z][y] for z in range(5)) for y in range(5)] for x in range(5)]

def Suma_Diagonal_Principal(matriz):
    return sum(matriz[x][x] for x in range(5))

def Suma_Diagonal_Inversa(matriz):
    return sum(matriz[x][4 - x] for x in range(5))

def Calcular_Media_Matriz(matriz):
    total_elementos = 5 * 5
    suma_elementos = sum(sum(fila) for fila in matriz)
    return suma_elementos / total_elementos

def menu():
    while True:
        Saludo()
        print("Menú:")
        print("************************************************************************************************")
        print("1. Primer punto (Vectores)")
        print("************************************************************************************************")
        print("2. Segundo punto (Matrices)")
        print("************************************************************************************************")
        print("3. Salir")
        print("************************************************************************************************")
        opcion = input("Por favor digite una opcion: ")
        print("************************************************************************************************")


        if opcion == "1":
            primer_vector = Vector_1()
            segundo_vector = Vector_Repet(primer_vector)
            print("Vector:", primer_vector)
            print("Vector sin repetir:", segundo_vector)
            numero = int(input("Ingrese un numero para mirar cuantas veces se repite:"))
            repeticiones = Cantidad_Repet(primer_vector, numero)
            print(f"El número {numero} se repite {repeticiones} veces en el vector.")
            print("Cantidad de elementos en el primer vector: ", len(primer_vector))
            print("Cantidad de elementos en el segundo vector sin repetir: ", len(segundo_vector))

        elif opcion == "2":
            Matriz_uno = Primer_Matriz()
            Matriz_dos = Segunda_Matriz(Matriz_uno)
            print("Primer matriz: ")
            for fila in Matriz_uno:
                print(fila)
            print("Segunda matriz: ")
            for fila in Matriz_dos:
                print(fila)
            print("Suma de filas de la primer matriz: ", SumarCada_Fila(Matriz_uno))
            print("Suma de columnas de la primer matriz: ", SumarCada_Columna(Matriz_uno))
            print("Resta de las matrices: ")
            for fila in Resta_Matrices(Matriz_uno, Matriz_dos):
                print(fila)
            numero = int(input("Ingrese un número para multiplicar la primer matriz: "))
            Matriz_uno_multiplicada =Multiplicar_Matriz_Numero(Matriz_uno, numero)
            print("Primer matriz multiplicada por el número: ")
            for fila in Matriz_uno_multiplicada:
                print(fila)
            print("Producto de las matrices:")
            Matriz_producto = Multiplicar_Matrices(Matriz_uno, Matriz_dos)
            for fila in Matriz_producto:
                print(fila)
            print("Suma de la diagonal principal de la matriz uno: ", Suma_Diagonal_Principal(Matriz_uno))
            print("Suma de la diagonal inversa de la matriz dos: ", Suma_Diagonal_Inversa(Matriz_dos))
            print("Media de todos los elementos de la matriz multiplicación: ", Calcular_Media_Matriz(Matriz_producto))

        elif opcion == "3":
            print("Gracias por usar el programa :)")
            print("************************************************************************************************")
            break

        else:
            print("Digite otro número (Opcion invalida)")
            print("************************************************************************************************")


menu()

