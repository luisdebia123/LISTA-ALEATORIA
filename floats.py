# Lista Aleatoria #
from colorama import init 
import random

from os import system
system("cls")



print ()
print ("8. Cree un tercer script floats.py que contenga una modificación del")
print ("Código Base de tal forma que en lugar de strings, lista contenga sólo")
print ("números flotantes aleatorios entre 10 y 50 con 3 decimales.")
print ("-------------------------------------------------------")
print ()
caracteres ='0123456789'
lista = []
for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(10, 50)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)


suma =0
for c in lista :
    numero = float(c)
    numero= numero/1000
    print(numero)
    suma = suma + numero
    promedio = suma/100

print()
print (promedio)



