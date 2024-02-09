price = 20
print(price)

#para ejecutar un fichero, en la TERMINAL escibimos python3 + nombre_del_fichero
#para guardar, hacemos CRTL + S
#para limpiar la terminal, usamos CLEAR

a = 5
b = 2.5

#el valor A es INTEGRER y el valor B es un FLOAT
suma = a + b
print(suma)

#podemos tambien definir PALABRAS dentro de las variables, SIEMPRE entre " o '
c = "Hola Estudiantes"
print(c)

#valores BOOLEANOS (true y false)
#son palabras reservadas por python, por tanto, no se les pueden asignar a variables
e = False
f = True

y_logico = e and f
print(y_logico)
#nos devuelve FALSE porque los dos conceptos NO son iguales

e = True
f = True

x_logico = e and f
print(x_logico)
#nos devuelve TRUE porque las dos variables son iguales

o_logico = e or f
print(o_logico)
#como uno de los dos valores son ciertos, nos devuelve TRUE. Solo se tiene que cumplir uno de ellos. 

negacion = not e
print(negacion)
#invertimos el valor de e, nos devuelve FALSE 

#tipo de variables, LISTAS
#podmeos poner diferentes conceptos dentro de una lista, des de numeros a palabras. 
numbers = [1,2,3,4,5,6]
print(numbers)

numbers.append("Alberto") #nos añade al final de la lista un concepto nuevo
print(numbers)

numbers.remove(1) #eliminamos el elemento que metemos entre los paréntesis
print(numbers)

#tipo de variables, DICCIONARIOS, lista de atributos asociados a un elemento
#asociamos valores de llave por valor --> key : value
person = {"Nombre" : "Lucia","Edad" : 25}
print(person)

print(person["Edad"]) #asi solo nos muestra el valor de edad

#otros conceptos
#Podemos sumar valores integrers con valores string?

nombre = "Lucia"
edad = 25

persona = nombre + edad
print(persona) #nos salta error, ya que no puede sumar con dos tipos de datos diferentes. 