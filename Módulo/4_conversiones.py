#Modificar variables de un tipo a otro
#TEXTO
a = 3
b =str(a)
print(b,type(b))

#ENTERO
a = int(7.8)
print(a)

#DECIMAL
a = float(7)
print(a)

#Libreria de Python
import math
a = round(7.8) #a partir del 0.5
print(a)

a = round(7.858745,2)
print(a)

a = math.ceil(7.4) #entera a la alza
print(a)

a = math.floor(7.8) #a la baja
print(a)

#Ejemplo de error
print(1.1+2.2) #guarda el dato de forma algo incorrecta
#Solucion
from decimal import *
getcontext().prec = 28
print(Decimal(1.1) + Decimal(2.2))

getcontext().prec = 56
print(Decimal(1.1) + Decimal(2.2))

getcontext().prec = 156 #vamos incrementando la precisión
print(Decimal(1.1) + Decimal(2.2))
