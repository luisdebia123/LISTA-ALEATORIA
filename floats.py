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
    largo = random.randint(1,2)  
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
        enteros=int(string_aleatorio)
        if enteros >9 and enteros<51 :
            lista.append(enteros)

Valor_Max= max([lista])

promedio=0
suma =0
cont=0
for c in lista :
    numero = (c)
    if numero>cont :
        cont=numero
    print(numero)
    suma = suma + numero
    promedio = suma/100

print()
print ('Suma de los Numeros : ',suma)
print()
print('Promedio  : ',promedio)
print()
print(Valor_Max)
print('Valor Máximo :',cont)
print('--------------------------------')
suma =0
for c in lista :
    numero = (c)
    print('numeros enteros entre 10 y 50 :',numero,'Menos valor promedio ',promedio,"  ", 
    round(numero-promedio,3))
