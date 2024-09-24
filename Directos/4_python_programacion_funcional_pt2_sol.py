# EJERCICIO 7:
# Definición de la función
def procesar_datos(operacion, *args, **kwargs):
    """
    Función que procesa una serie de datos dependiendo del tipo de operación especificada.

    Parámetros:
    - operacion (str): Tipo de operación a realizar ('sumar', 'restar', 'multiplicar', 'dividir').
    - *args: Argumentos posicionales que representan los datos sobre los cuales se realizará la operación.
    - **kwargs: Argumentos de palabra clave que especifican opciones adicionales para la operación.

    Retorna:
    - float: El resultado de la operación realizada sobre los datos.
    """
    # Verificamos el tipo de operación especificada
    if operacion == 'sumar':
        # Sumar los datos proporcionados
        suma_total = kwargs.get('valor_inicial', 0)  # Valor inicial para la suma (si se proporciona)
        for dato in args:
            suma_total += dato
        return suma_total
    elif operacion == 'restar':
        # Restar los datos proporcionados
        resultado_resta = args[0]  # Inicializamos con el primer valor
        for dato in args[1:]:
            resultado_resta -= dato
        return resultado_resta
    elif operacion == 'multiplicar':
        # Multiplicar los datos proporcionados
        factor_multiplicacion = kwargs.get('factor', 1)  # Factor de multiplicación (si se proporciona)
        resultado_multiplicacion = factor_multiplicacion
        for dato in args:
            resultado_multiplicacion *= dato
        return resultado_multiplicacion
    elif operacion == 'dividir':
        # Dividir los datos proporcionados
        resultado_division = args[0]  # Inicializamos con el primer valor
        for dato in args[1:]:
            resultado_division /= dato
        return resultado_division
    else:
        # Levantamos una excepción si la operación no es válida
        raise ValueError("Operación no válida: {}".format(operacion))
    
# Ejemplo de uso
resultado_suma = procesar_datos('sumar', 1, 2, 3, 4, valor_inicial=10)
print("Resultado de la suma:", resultado_suma) # Output: Resultado de la suma: 20

resultado_resta = procesar_datos('restar', 20, 5, 3)
print("Resultado de la resta:", resultado_resta) # Output: Resultado de la resta: 12

resultado_multiplicacion = procesar_datos('multiplicar', 2, 3, 4, factor=2)
print("Resultado de la multiplicación:", resultado_multiplicacion) # Output: Resultado de la multiplicación: 48

resultado_division = procesar_datos('dividir', 100, 5, 2)
print("Resultado de la división:", resultado_division) # Output: Resultado de la división: 10.0



# EJERCICIO 8:
# Creamos una lista de cadenas de caracteres
lista_palabras = ["Hola", "python", "es", "el", "mejor", "lenguaje", "de", "programación"]

# Utilizamos la función sorted() para ordenar la lista de palabras
# Utilizamos el parámetro key para especificar que queremos ordenar según la longitud de cada palabra
# La función lambda x: len(x) devuelve la longitud de cada palabra x
# Esto ordenará la lista de palabras de menor a mayor longitud
palabras_ordenadas = sorted(lista_palabras, key=lambda x: len(x))

# Imprimimos la lista ordenada
print(palabras_ordenadas)
# Output: ['es', 'el', 'de', 'Hola', 'mejor', 'python', 'lenguaje', 'programación']


# EJERCICIO 9:
# Creamos una lista de números
numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Utilizamos una expresión de lista para filtrar los elementos de la lista numbers
# Aplicamos una condición personalizada para seleccionar los elementos que son mayores que 10 y múltiplos de 3
# La condición x > 10 and x % 3 == 0 verifica si el número x es mayor que 10 y también es divisible por 3
filtered_numbers = [x for x in numbers if x > 10 and x % 3 == 0]

# Imprimimos la lista resultante después de aplicar el filtro
print(filtered_numbers)

# Output: [12, 15, 18, 21, 24, 27, 30]


# EJERCICIO 10:
# Creamos un diccionario que contiene nombres como claves y edades como valores
people = {"Alice": 30, "Bob": 25, "Charlie": 35, "David": 40}

# Utilizamos la función sorted() para ordenar los elementos del diccionario según el valor de la edad.
# Utilizamos el parámetro key para especificar la función que determina el criterio de ordenación.
# Definimos una función lambda que toma un elemento (clave-valor) y devuelve el valor de la edad (segundo elemento).
# Esto ordenará el diccionario por edad de menor a mayor.
sorted_people = dict(sorted(people.items(), key=lambda x: x[1]))

# Imprimimos el diccionario ordenado
print(sorted_people)

# Output: {'Bob': 25, 'Alice': 30, 'Charlie': 35, 'David': 40}

# EJERCICIO 11:
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5]

# Utilizamos la función map() junto con una lambda para elevar al cuadrado cada número en la lista
# La lambda x: x**2 eleva al cuadrado cada número x
# La función map() aplica la lambda a cada elemento de la lista y devuelve un iterable
# Convertimos el resultado de map() en una lista para obtener los números elevados al cuadrado
squared_numbers = list(map(lambda x: x**2, numbers))

# Imprimimos la lista resultante que contiene los números elevados al cuadrado
print(squared_numbers) # Output : [1, 4, 9, 16, 25]

# Output: [1, 4, 9, 16, 25]

# EJERCICIO 12:
 # Creamos una lista de números
numbers = [1, 2, 6, 7, 8, 3, 9, 10, 13]

# Utilizamos la función filter() junto con una lambda para filtrar los números mayores que 5
# La lambda lambda x: x > 5 devuelve True si el número x es mayor que 5, de lo contrario False
# La función filter() filtra los elementos de la lista que cumplen la condición dada por la lambda
# Convertimos el resultado de filter() en una lista para obtener los números que cumplen la condición
filtered_numbers = list(filter(lambda x: x > 5, numbers))

# Utilizamos la función len() para contar cuántos elementos hay en la lista filtrada
count_greater_than_5 = len(filtered_numbers)

# Imprimimos la cantidad de números que son mayores que 5
print(count_greater_than_5) # Output: 5

# Output: 6