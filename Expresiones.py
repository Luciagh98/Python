#a través de expresiones, podemos guardar métodos. 

#EXPRESIONES ARITMÉTICAS
a = 5 + 2 #utilizamos una expresión, en este caso +, para obtener unos valores
z = 15 - 2 

#EXPRESIONES LÓGICAS
b = (10<20) #las expresiones lógicas nos permiten comparar, y nos devuelven TRUE o FALSE
print(b)

c = (10<5)
print(c)

#EXPRESIONES DE CADENA
d = "Bienvenido" + " " + "Estudiante" #almacenamos la concatenación de los dos valores
print(d)

#EXPRESSIONES LLAMADA A LA FUNCIÓN
e = len("Hola") #nos devuelve la longitud de la cadena de texto
print(e)

#_______________________________
#OPERADORES ARITMÉTICOS
valor1 = 30
valor2 = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

#cuando tenemos divisiones con muchos decimales, podemos definir el número de decimales o el redondeo a la baja
division2 = a // b

#OPERADORES DE ASSIGNACIÓN
valor3 = 5
valor3 = 10 #podmeos ir assignando valores diferentes a la variable
valor3 += 2 #nos contempla el valor definido, 10, más el valor nuevo, 2
valor3 -= 5 #nos contempla el valor definido, 10, menos el valor nuevo, 5

#OPERADORES DE COMPARACIÓN
#el valor que nos devuelve, será siempre TRUE o FALSE. 
valor4 = 10
valor5 = 20

es_igual = valor4 == valor5
print(es_igual) #nos devuelve FALSE ya que los dos valores no son iguales

no_es_igual = valor4 != valor5
print(no_es_igual)# nos devuelve TRUE ya que los dos valores no son iguales

menor_que = valor4 < valor5
print(menor_que) #nos devuelve TRUE porque es cierto. Tambien válido <=.

mayor_que = valor4 > valor5
print(mayor_que) #nos devuelve FAlse porque no es cierto. Tambien válido >=.

#OPERADORES LÓGICOS
valor6 = True
valor7 = False

and_logico = valor6 and valor7
print(and_logico) #nos devuelve FALSE porque los dos valores NO son iguales

or_logico = valor6 or valor7
print(or_logico) #nos devuelve TRUE porque uno de los dos son ciertos. 

not_logico = not valor7
print(not_logico) # nos devuelve TRUE porque nos cambia el valor de valor7