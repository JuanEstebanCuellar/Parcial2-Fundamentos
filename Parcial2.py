#Parcial 2 (Fundamentos de la programacion)
#Integrantes: Christopher Villa - Juan Esteban Cuellar Trujillo -  Juan Jose Vallejo
#Fecha: 12  de octubre del 2023

import random

#Variables:

Vectores=[]
vector_sin_repetir = []
numero=0

def Vectores1 ():
    for x in range (50):
        NumerosVectores=random.randint(0,20)
        Vectores.append(NumerosVectores)
    print("***********************************************")
    print("Vectores del 1 al 50:")
    print(Vectores)

def eliminar_duplicados():
    vector_sin_repetir = list(set(Vectores))
    print("***********************************************")
    print("Vectores 1 sin repetir:")
    print(vector_sin_repetir)

def contar_repeticiones(numero, Vectores):
    contador = 0
    for elemento in Vectores:
        if elemento == numero:
            contador += 1
    print("***********************************************")
    print("Cantidad de veces que se repiten los numeros:")
    print(contador)

Vectores1()
eliminar_duplicados()
contar_repeticiones(numero, Vectores)