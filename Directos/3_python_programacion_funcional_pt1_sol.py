# EJERCICIO 1:
# Definición de la función:
def frecuencia_letras(cadena):
    """
    Función que cuenta la frecuencia de cada letra en una cadena de texto, ignorando los espacios.
    
    Parámetros:
    - cadena (str): La cadena de texto en la que se contará la frecuencia de letras.
    
    Retorna:
    - dict: Un diccionario con las frecuencias de cada letra en la cadena.
    """
    # Creamos un diccionario para almacenar la frecuencia de cada letra
    frecuencia = {}
    
    # Iteramos sobre cada caracter en la cadena
    for caracter in cadena:
        # Ignoramos los espacios
        if caracter != ' ':
            # Contamos la frecuencia de cada letra y la almacenamos en el diccionario
            # Si la letra ya está en el diccionario, incrementamos su frecuencia en 1
            # Si no está, inicializamos su frecuencia en 1
            frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    
    # Devolvemos el diccionario con las frecuencias de las letras
    return frecuencia

# Caso de uso:
letras_cadena = "El patio de mi casa es particular, cuando llueve se moja como los demás"
print(frecuencia_letras(letras_cadena))
# Output: 
#{'E': 1, 'l': 5, 'p': 2, 'a': 7, 't': 2, 'i': 3, 'o': 6, 'd': 3, 'e': 6, 'm': 4, 'c': 4, 's': 5, 'r': 2, 'u': 3, ',': 1, 'n': 1, 'v': 1, 'j': 1, 'á': 1}


# EJERCICIO 2:
# Definición de la función:
def buscar_palabra(lista_palabras, palabra_objetivo):
    """
    Función que busca una palabra objetivo en una lista de palabras.
    
    Parámetros:
    - lista_palabras (list): La lista de palabras en la que se realizará la búsqueda.
    - palabra_objetivo (str): La palabra que se desea buscar.
    
    Retorna:
    - list: Una lista con todas las palabras de la lista original que contienen la palabra objetivo.
    """
    # Inicializamos una lista vacía para almacenar las palabras que contienen la palabra objetivo.
    palabras_encontradas = []
    
    # Iteramos sobre cada palabra en la lista de palabras.
    for palabra in lista_palabras:
        # Comprobamos si la palabra objetivo está contenida en la palabra actual.
        if palabra_objetivo in palabra:
            # Si la palabra objetivo está presente en la palabra actual, añadimos esa palabra a la lista.
            palabras_encontradas.append(palabra)
    
    # Devolvemos la lista que contiene todas las palabras de la lista original que contienen la palabra objetivo.
    return palabras_encontradas

# Ejemplo de uso:
lista_palabras = ["manzana", "banana", "naranja", "melocotón", "plátano"]
palabra_objetivo = "na"
palabras_encontradas = buscar_palabra(lista_palabras, palabra_objetivo)
print(palabras_encontradas)
# Output: ['manzana', 'banana', 'naranja']


# EJERCICIO 3:
# Definición de la función:
def calcular_promedio(lista, nota_aprobado=5):
    """
    Función que calcula el promedio de una lista de números y determina si es aprobado o suspenso.
    
    Parámetros:
    - lista (list): La lista de números de la cual se calculará el promedio.
    - nota_aprobado (int): La nota mínima para considerar aprobado. Por defecto, es 5.
    
    Retorna:
    - tuple: Una tupla que contiene el promedio de los números y el estado de aprobado o suspenso.
    """
    # Calculamos la media
    media = sum(lista) / len(lista) if len(lista) > 0 else 0
    
    # Determinamos el estado
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    # Devolvemos una tupla con la media y el estado
    return (media, estado)

# Ejemplo de uso:
notas_alumnos = [6, 7, 8, 4, 5]
resultado = calcular_promedio(notas_alumnos)
print(resultado) # Output: (6.0, 'aprobado')


# EJERCICIO 4:
# Definición de la función:
def factorial(n):
    """
    Función que calcula el factorial de un número utilizando recursividad.
    
    Parámetros:
    - n (int): Número entero positivo del cual se calculará el factorial.
    
    Retorna:
    - int: El factorial del número especificado.
    """
    # Verificamos si el número es igual a 0
    if n == 0:
        # Si es igual a 0, devolvemos 1 (por definición, el factorial de 0 es 1)
        return 1
    else:
        # Si el número es diferente de 0, calculamos el factorial recurriendo a la función factorial() con n-1
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado_factorial = factorial(numero)
print("El factorial de", numero, "es:", resultado_factorial) # Output: El factorial de 5 es: 120



# EJERCICIO 5:
# Definición de la función:
def combinar_listas(*args):
    """
    Función que combina un número arbitrario de listas utilizando los índices como claves.
    
    Parámetros:
    - *args (list): Un número arbitrario de listas a combinar.
    
    Retorna:
    - dict: Un diccionario donde las listas originales se combinan utilizando los índices como claves.
    """
    # Creamos un diccionario para almacenar las listas combinadas
    lista_combinada = {}
    
    # Iteramos simultáneamente sobre todas las listas utilizando la función zip
    for indice, elementos in enumerate(zip(*args)):
        # Asignamos el índice como clave y la lista combinada como valor en el diccionario
        lista_combinada[indice] = list(elementos)
    
    # Devolvemos el diccionario combinado
    return lista_combinada

# Ejemplo de uso:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

resultado = combinar_listas(lista1, lista2, lista3)
print(resultado) # Output: {0: [1, 'a', True], 1: [2, 'b', False], 2: [3, 'c', True]}


# EJERCICIO 6:
# Definición de la función:
def area_figura(**kwargs):
    """
    Función que calcula el área de una figura geométrica según el tipo especificado.
    
    Parámetros:
    - **kwargs (dict): Argumentos clave-valor donde la clave representa el tipo de figura geométrica y los valores son los argumentos necesarios para calcular el área de esa figura.
    
    Retorna:
    - float: El área calculada de la figura geométrica especificada.
    """
    # Verificamos si se proporcionaron suficientes argumentos para determinar automáticamente el tipo de figura
    if 'base' in kwargs and 'altura' in kwargs:
        # Si se proporcionan base y altura, asumimos que es un triángulo
        base = kwargs['base']
        altura = kwargs['altura']
        area = (base * altura) / 2  # Calculamos el área del triángulo utilizando la fórmula A = (base * altura) / 2
    elif 'radio' in kwargs:
        # Si se proporciona el radio, asumimos que es un círculo
        radio = kwargs['radio']
        area = 3.14 * (radio ** 2)  # Calculamos el área del círculo utilizando la fórmula A = πr^2
    elif 'lado' in kwargs:
        # Si se proporciona el lado, asumimos que es un cuadrado
        lado = kwargs['lado']
        area = lado ** 2  # Calculamos el área del cuadrado utilizando la fórmula A = L^2
    else:
        raise ValueError("No se pudo determinar el tipo de figura geométrica.")  # Levantamos una excepción si no se puede determinar el tipo de figura
    
    return area

# Ejemplo de uso:
area_triangulo = area_figura(base=3, altura=4)
print("Área del triángulo:", area_triangulo) # Output: Área del triángulo: 6.0

area_circulo = area_figura(radio=2)
print("Área del círculo:", area_circulo) # Output: Área del círculo: 12.56

area_cuadrado = area_figura(lado=5)
print("Área del cuadrado:", area_cuadrado) # Output: Área del cuadrado: 25
