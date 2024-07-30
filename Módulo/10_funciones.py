# función sin parámetros o retorno de valores
def diHola():
    print("¡Hola!")
diHola() # llamada a la función, '¡Hola!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
    print("¡Hola " + name + "!")
holaConNombre("Ana") # llamada a la función, '¡Hola Ana!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2
multiplica(3, 5) # muestra 15 en la consola

def suma(a,b):
    return a + b

print("suma(a,b)=", suma(16,9))

sumalambda = lambda a, b : a + b
print("sumalambda(a,b)=", sumalambda(16,9))

def resta (a:int, b:int) -> float:
    """
    Se resta el numero al a menos el numero b
    Args:
      a (int): Primer numero a restar
      b (int): Segundo numero
    Returns:
      Resta de los numeros
    """
    return a - b