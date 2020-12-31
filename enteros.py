# Lista Aleatoria #

import random
import os
os.system('cls')

from os import system
system("cls")
suma =0

print ()
print ("5. Cree un segundo script enteros.py")
print ()
caracteres =('0123456789')
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)
    
print(lista)

print()

print ("6. Calcule el promedio de los valores numéricos de lista. .")
print ()
print ("------------------------------------")


largo_lista2 = len (lista)
suma_elemento = 0
n=0
v = 0   
while  n != largo_lista2 :
    suma_elemento = suma_elemento +int (lista [n])
    n=n+1
promedio = (suma_elemento/largo_lista2)
print ("Suma Total de  Elementos Lista2   ",promedio)
promedio = round( suma_elemento/largo_lista2)
print ("Promedio  Enteros Lista2   ",promedio)

print()
print("7. Actualice lista, restando el promedio a todos los elementos de ésta")
print ("---------------------------------------------------------------------")


for z in lista:
    resta= int(z)
    resta= resta-promedio
    print (resta)
    