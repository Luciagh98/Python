# Importamos las clases datetime y timedelta desde el módulo datetime
from datetime import datetime, timedelta  

# Definimos la clase Libro
class Libro:  
    """
    Clase para representar un libro genérico.
    """
    # Definimos el método de inicialización de la clase
    def __init__(self, titulo, autor, precio):  
        """
        Inicializa un libro con su título, autor y precio.

        Parámetros:
        - titulo (str): El título del libro.
        - autor (str): El autor del libro.
        - precio (float): El precio del libro.
        
        Retorna:
        - None
        """
        # Asignamos el título del libro al atributo 'titulo'
        self.titulo = titulo  
        # Asignamos el autor del libro al atributo 'autor'
        self.autor = autor  
        # Asignamos el precio del libro al atributo 'precio'
        self.precio = precio  
        # Inicializamos la cantidad en 0 al crear el libro
        self.cantidad = 0  
    # Definimos un método para establecer la cantidad de libros disponibles
    def establecer_cantidad(self):  
        """
        Método para establecer la cantidad de libros disponibles.

        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Iniciamos un bucle infinito para solicitar la cantidad hasta que sea válida
        while True:  
            try:
                 # Solicitamos la cantidad al usuario
                cantidad = int(input(f'Ingrese la cantidad de libros de {self.titulo}: ')) 
                # Comprobamos si la cantidad es negativa
                if cantidad < 0:  
                    # Imprimimos un mensaje de error
                    print("La cantidad no puede ser negativa. Intente de nuevo.")  
                else:
                    # Asignamos la cantidad al atributo 'cantidad'
                    self.cantidad = cantidad
                    # Salimos del bucle 
                    break  
            # Capturamos la excepción si el usuario ingresa un valor no válido
            except ValueError: 
                # Imprimimos un mensaje de error 
                print("Por favor, ingrese un número entero válido.") 

    # Definimos un método para obtener información detallada del libro    
    def info_libro(self):  
        """
        Método para obtener información detallada del libro.

        Parámetros:
        - Ninguno
        
        Retorna:
        - str: Información del libro incluyendo título, autor, precio y cantidad disponible.
        """
        # Inicializamos una cadena vacía para almacenar la información
        info = ""  
        # Añadimos el título del libro a la cadena
        info += "Título: " + self.titulo + "\n" 
        # Añadimos el autor del libro a la cadena 
        info += "Autor: " + self.autor + "\n" 
        # Añadimos el precio del libro a la cadena y lo convertimos a string 
        info += "Precio: " + str(self.precio) + "\n"
        # Añadimos la cantidad disponible del libro a la cadena y la convertimos a string  
        info += "Cantidad: " + str(self.cantidad) + "\n"  
        # Retornamos la cadena con la información del libro
        return info  

# Definimos la clase LibroFisico que hereda de la clase Libro
class LibroFisico(Libro):  
    """
    Clase para representar un libro físico, hereda de la clase Libro.
    """
    # Definimos el método de inicialización de la clase
    def __init__(self, titulo, autor, precio, categoria, peso):  
        """
        Inicializa un libro físico con título, autor, precio, categoría y peso.

        Parámetros:
        - titulo (str): El título del libro.
        - autor (str): El autor del libro.
        - precio (float): El precio del libro.
        - categoria (str): La categoría del libro.
        - peso (str): El peso del libro.
        
        Retorna:
        - None
        """
         # Llamamos al método de inicialización de la clase padre
        super().__init__(titulo, autor, precio) 
        # Asignamos la categoría del libro físico al atributo 'categoria'
        self.categoria = categoria
        # Asignamos el peso del libro físico al atributo 'peso'  
        self.peso = peso 

    # Definimos un método para calcular la fecha estimada de entrega
    def envio(self, dias_envio=5):  
        """
        Método para calcular la fecha estimada de entrega.

        Parámetros:
        - dias_envio (int): El número de días estimados para el envío (predeterminado: 5).
        
        Retorna:
        - datetime: La fecha estimada de entrega.
        """
        # Obtenemos la fecha y hora actual
        hoy = datetime.now()  
        # Calculamos la fecha estimada de entrega sumando días_envio a la fecha actual
        fecha_entrega = hoy + timedelta(days=dias_envio)  
        # Retornamos la fecha estimada de entrega
        return fecha_entrega  
    
    # Definimos un método para obtener información detallada del libro físico
    def info_libro(self):  
        """
        Método para obtener información detallada del libro físico.

        Parámetros:
        - Ninguno
        
        Retorna:
        - str: Información del libro físico incluyendo título, autor, precio, categoría, peso y fecha de entrega estimada.
        """
        # Llamamos al método info_libro de la clase padre para obtener la información básica del libro
        info_libro = super().info_libro()
        # Añadimos la categoría del libro físico a la cadena  
        info_libro += "Categoría:  " + self.categoria + "\n"
        # Añadimos el peso del libro físico a la cadena y lo convertimos a string  
        info_libro += "Peso: " + str(self.peso) + "\n" 
        # Añadimos la fecha de entrega estimada a la cadena en formato YYYY-MM-DD 
        info_libro += "Fecha de entrega: " + str(self.envio().strftime("%Y-%m-%d")) + "\n" 
        # Retornamos la cadena con la información del libro físico 
        return info_libro 
     
# Definimos la clase AudioLibro que hereda de la clase Libro
class AudioLibro(Libro):  
    """
    Clase para representar un audiolibro, hereda de la clase Libro.
    """
    # Definimos el método de inicialización de la clase
    def __init__(self, titulo, autor, precio, categoria, duracion):  
        """
        Inicializa un audiolibro con título, autor, precio, categoría y duración.

        Parámetros:
        - titulo (str): El título del libro.
        - autor (str): El autor del libro.
        - precio (float): El precio del libro.
        - categoria (str): La categoría del libro.
        - duracion (int): La duración del audiolibro en segundos.
        
        Retorna:
        - None
        """
        # Llamamos al método de inicialización de la clase padre
        super().__init__(titulo, autor,  precio)  
        # Asignamos la categoría del audiolibro al atributo 'categoria'
        self.categoria = categoria 
        # Asignamos la duración del audiolibro al atributo 'duracion' 
        self.duracion = duracion  
    
    # Definimos un método para convertir la duración del audiolibro a formato HH:MM:SS
    def obtener_duracion(self):  
        """
        Método para convertir la duración del audiolibro a formato HH:MM:SS.

        Parámetros:
        - Ninguno
        
        Retorna:
        - str: La duración del audiolibro en formato HH:MM:SS.
        """
        # Calculamos las horas dividiendo la duración total por 3600 segundos
        horas = str(self.duracion // 3600) 
        # Calculamos los minutos dividiendo el resto de la división entera de la duración por 3600 por 60 
        minutos = str((self.duracion % 3600) // 60) 
        # Calculamos los segundos como el resto de la división entera de la duración por 60 
        segundos = str(self.duracion % 60)  
        # Concatenamos las partes de la duración en un formato de hora HH:MM:SS
        duracion_format = horas + ":" + minutos + ":" + segundos 
        # Retornamos la duración en formato HH:MM:SS 
        return duracion_format  
    
    # Definimos un método para obtener información detallada del audiolibro
    def info_libro(self):  
        """
        Método para obtener información detallada del audiolibro.

        Parámetros:
        - Ninguno
        
        Retorna:
        - str: Información del audiolibro incluyendo título, autor, precio, categoría, duración y duración en formato HH:MM:SS.
        """
        # Llamamos al método info_libro de la clase padre para obtener la información básica del libro
        info_libro = super().info_libro()
        # Añadimos la categoría del audiolibro a la cadena  
        info_libro += "Categoría:  " + self.categoria + "\n" 
        # Añadimos la duración del audiolibro en segundos a la cadena y lo convertimos a string 
        info_libro += "Duración en segundos: " + str(self.duracion) + "\n"  
        # Añadimos la duración del audiolibro en formato HH:MM:SS a la cadena llamando al método obtener_duracion
        info_libro += "Duración: " + self.obtener_duracion() + "\n"
        # Retornamos la cadena con la información del audiolibro  
        return info_libro

