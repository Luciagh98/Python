#nos permiten iterar sobre unos valores, mostrando lo que deseamos.

nombres = ["David","Lucia","Arnedo","Garcia",5]

for elemento in nombres:
  print(elemento)

#nos imprime los elementos en filas, "quitandolo" de la lista.
  
nombres = ["David","Lucia","Arnedo","Garcia",5]
position = 1

for elemento in nombres:
  print(position)
  position += 1
  print(elemento)

# de esta manera imprimimos la posicion de cada elemento en la lista, seguido del nombre como tal.
  
nombres = ["David","Lucia","Arnedo","Garcia"]

for elemento in nombres:
  print(elemento + " Nombre")

#también podemos añadir cosas nuevas al elemento impreso.

s = "Hola Estudiantes"

for letra in s:
  print(letra)

#también podemos imprimir las letras de una frase (string)
  
#el bucle WHILE funciona mediente si se cumplen esas condicones

i = 1

while i <= 5 :
  print(i)
  i +=1
#hay que establecer una condición final para que termine el bucle.
  
#__________________EJEMPLOS PRÁCTICOS_____________________________
  
#Queremos saber el valor total de nuestra lista de la compra:
#No hay condición --> FOR
  
patatas = 5
tomates = 3
naranjas = 7

productos = [patatas,tomates,naranjas]
print(productos)

total = 0 #necesitamos definir una variable previa que nos vaya contemplando la suma de valores.

for producto in productos:
  total += producto
  print(total) #si lo metemos dentro del bucle, nos va sumando los valores uno a uno, creando 3 valores nuevos
print(total) #si lo ponemos fuera, nos muestra el valor total solo

#Queremos saber si vamos haciendo todas las tareas que tenemos que hacer durante el dia:
#Que se cumpla la condición de 0 --> WHILE

tareas = ["T1","T2","T3","T4"]

while len(tareas) > 0: #mientras sea mayor que 0, significa que hay tareas pendientes:
  tarea_actual = tareas.pop(0) #le indicamos la posición de la tarea que queremos quitar
  print(f"Estoy completando la tarea {tarea_actual}.") #vamos imnprimiendo las tareas pendientes que estamos haciendo en el momento
print("Puedes ver Netflix.") #al final de todas las tareas hechos, imprimimos el caso final

#Queremos sacar los valores de un diccionario con descripciones de estudiantes:
#No hay condición --> FOR

estudiante = {"Nombre" : "Lucia", "Apellido" : "Garcia"}

for clave, valor in estudiante.items(): #clave, valor es la definicion de diccionario. La función de items nos permite sacar el valor del diccionario
  print(clave, ":", valor) #imprimimos cada elemento del diccionario separado por :

#tenemos que poner clave, valor en el bucle ya que tenemos dos elementos en el diccionario. Si solo queremos obtener el valor, seria:
  
for clave, valor in estudiante.items():
  print(valor)


#__________________UNIR ELEMENTOS__________________________
  
numeros = [5,8,10,-3,2,1]

for numero in numeros:
  print (numero)
  if numero < 0:
    print("El primer número negativo encontrado es: ", numero)
    break

#Tenemos una lista de números, tanto positivos como negativos y queremos encontrar el primer negativo. Dentro de un bucle FOR, le pedimos que nos imprima (PRINT) los números, y dentro del bucle ponemos un condicionante (IF) que nos encuentre el primer numero negativo (numero<0). Quando encuentre ese numero = se cumpla la condición if, queremos que imprima (PRINT) la frase y el numero. 

#El concepto de break significa que "rompa", es decir, que termine el bucle una vez cumplida la condición.

numeros = [5,8,10,-3,2,1]

for numero in numeros:
  print (numero)
  if numero < 0:
    print("El primer número negativo encontrado es: ", numero)
    #sin el break, nos termina de iterar la lista hasta el final