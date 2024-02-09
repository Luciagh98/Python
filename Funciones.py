#Las funciones nos permiten crear acciones (que podrian ser repetitivas) en una única definición. 

#Queremos saludar de forma rápida:

def greeting():
  print("Buenos días")

greeting() #con esta función hecha, ya podemos poner directamente greeting()para que nos imprima lo definido en la función, sin tener que ir escribiendo todo el rato el PRINT. 

#Queremos hacer una función que nos diga que productos tenemos que comprar:

def buy(list):
  print(f"Mi lista a comprar: {list}")

buy(["patatas","huevos","cebolla","aceite"]) #queremos que nos meta esta lista en la frase de la función.
#Si metieramos la lista de productos dentro de la función, no podriamos cambiar los elementos:
buy(["camiseta","zapatillas","calcetines"])

def buy(list,budget):
  print(f"Mi lista a comprar: {list} | pressupuesto: {budget}")

buy(["patatas","huevos","cebolla","aceite"], 100)
buy(["camiseta","zapatillas","calcetines"], 600)

#Si pasamos los parámetros al revés:
buy(300, ["camiseta","zapatillas","calcetines"],) #nos gira los parámetros, ya que entiende que el número es la lista de productos y el segundo, la lista de productos, el pressupuesto.

#Si no le pasamos uno de los parámetros
buy(["camiseta","zapatillas","calcetines"]) #nos da un error, ya que le falta un argumento, en este caso el pressupuesto

#Queremos una función que nos vaya sumando los valores de una lista de la compra
def carrito_suma(list_price):
  total = 0
  for price in list_price:
    total += price
  return total

carrito_suma([5,2,7,9,8,10,27]) #De esta manera nos suma el valor de la lista
print(carrito_suma([5,2,7,9,8,10,27])) #Para que se muestre en pantalla

carrito_price = carrito_suma([5,2,7,9,8,10,27]) #Podemos asignarle una variable, para que nos retorne el resultado de la función
print(carrito_price)

carrito_price_two = carrito_suma([5,20,75,9,86,10,27]) #Ya le podemos asignar la función a otras variables con valores diferentes
print(carrito_price_two)

#Queremos saber cual es el mejor restaurante de una lista basado en las estrellas que tiene:

def best_restaurant_stars(stars_list):
  maximo = stars_list[0] #le pasamos que el valor maximo de la lista de estrellas es el que se situa en la posición 0
  for star in stars_list:
    if star > maximo:
      maximo = star
  return maximo

best_restaurant_stars([5,10,30,70,90,75,99])
best_restaurant = best_restaurant_stars([5,10,30,70,90,75,99])

print(best_restaurant)

#Hacemos una función basada en una lista de estrellas. Le asignamos el valor máximo, que en un inicio será aquel situado en la posicón 0 de la lista de estrellas. Definimos un bucle FOR que, por cada estrella en la lista de estrellas, nos mire si (IF) se cumple que si la estrella analizada es mayor que el valor assignado al máximo, nos acutalize el máximo al valor de la estrella. Obteniendo así (RETURN) el máximo de la lista de estrellas.


