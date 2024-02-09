#una estructura donde evaluamos si se cumple una condición, y dependiendo de ello que haga X acciones. 
x = 10

if x < 20:
  print("Este número es menor que 20.")
  print("Hola")

#teniendo el print dentro de la funcion nos lo imprime porque se cumple la condicion, en cambio, si lo imprimimos fuera lo hará porque es una orden que esta fuera del condicionante. 
  
if x < 5:
  print("Este número es menor que 20.")
print("Hola") 

#aqui solo nos imprime el HOLA, ya que no se cumple la condición para imprimir la primera frase. 

x = 2
if x < 5:
  print("Este número es menor que 5.")
else:
  print("Este número es mayor que 5.")

#añadimos el concepto de ELSE, para que nos haga otra cosa en caso de que no se cumpla la condición.

#podemos añadir diversos casos posibles al condicionante, irá pasando por los diversos casos hasta que encuentre uno que se cumpla. En el momento que se cumpla uno, ejecutará esa acción. 

x = 2
if x <= 5:
  print("Este número es menor o igual que 5.")
elif x ==10:
  print("Este número es igual a 10.")
else:
  print("Este número es mayor que 5.")

#dentro de los mismos condicionantes podemos meter más condicionantes, eso si, siempre IF.

x = 10
z = 20

if x < 5:
  print("Este número x es menor que 5.")
  if x ==10:
    print("Este número x es igual a 10.")
  elif z == 20:
    print("Este número z es igual a 20.")
else:
  print("Este número x es mayor que 5.")

#como no se cumple ya el primer condicionante x<5, ya no entra a revisar las condiciones del interior, sino que ya pasa al ELSE. 
