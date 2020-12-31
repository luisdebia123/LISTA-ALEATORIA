# Lista Aleatoria #
from colorama import init 
import random

from os import system
system("cls")

 

print ()
print ("1. Cree un script strings.py que contenga el código base")
print ()
caracteres ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)

print(lista)

print()
print ("2.- Lista con el largo de cada elemento string de lista")
print ("-------------------------------------------------------")
print()
n = 0
i = 0
largo = 0
lista2 = []
for n in range(0,100):
    string_aleatorio2 = ''
    largo2 = random.randint(1, 20)
    for i in range(0, largo2):
        string_aleatorio2 += random.choice(caracteres)
    lista2.append(string_aleatorio2)

for z in lista2:
    print (len(z), "   ",(z))


print ("3. Calcule el largo promedio de los strings en lista.")

largo_lista2 = len (lista2)
largo_elemento = 0
n=0
v = 0

while  n != largo_lista2 :
    largo_elemento = largo_elemento + len (lista2 [n])
    n=n+1
promedio = (largo_elemento/largo_lista2)
print ("Promedio Largo Elementos Lista2   ",promedio)
promedio = round( largo_elemento/largo_lista2)
print ("Promedio Largo Elementos Lista2   ",promedio)


print()
print ("4.- Lista a un largo igual a la parte entera del promedio calculado")
print()
for x in lista2:
    largo =(x)[1:12]
    n = len(largo)
    if n == 11:
        print(largo)