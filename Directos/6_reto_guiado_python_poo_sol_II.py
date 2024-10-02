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
    
 # Definimos la clase ECommerce     
class ECommerce:  
    """
    Clase para representar un sistema de comercio electrónico.
    """
    # Definimos el método de inicialización de la clase
    def __init__(self):  
        """
        Inicializa una instancia del sistema de comercio electrónico.

        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Inicializamos una lista vacía para almacenar los productos en el carrito
        self.carrito = []  
        # Inicializamos un diccionario vacío para almacenar el inventario de productos
        self.inventario = {}  

     # Definimos un método para agregar productos al inventario
    def agregar_al_inventario(self, producto): 
        """
        Método para agregar productos al inventario.

        Parámetros:
        - producto (objeto): El producto que se va a agregar al inventario.
        
        Retorna:
        - None
        """
        # Agregamos el producto al inventario con el título en minúsculas como clave
        self.inventario[producto.titulo.lower()] = producto

    # Definimos un método para agregar productos al carrito de compras
    def agregar_al_carrito(self, nombre_producto):  
        """
        Método para agregar productos al carrito de compras.

        Parámetros:
        - nombre_producto (str): El nombre del producto que se va a agregar al carrito.
        
        Retorna:
        - None
        """
        # Eliminamos los espacios en blanco y convertimos el nombre del producto a minúsculas
        nombre_producto = nombre_producto.strip().lower()
        # Verificamos si el producto está en el inventario  
        if nombre_producto in self.inventario:
            # Obtenemos el objeto del producto del inventario  
            producto = self.inventario[nombre_producto]
            # Verificamos si hay suficientes unidades del producto en el inventario  
            if self.inventario[nombre_producto].cantidad > 0:
                # Agregamos el producto al carrito de compras  
                self.carrito.append(self.inventario[nombre_producto])
                # Reducimos la cantidad disponible del producto en el inventario  
                self.inventario[nombre_producto].cantidad -= 1
                # Imprimimos un mensaje de éxito  
                print(f"{nombre_producto} ha sido agregado al carrito. Precio: {producto.precio}")  
            else:
                # Imprimimos un mensaje de error
                print(f"No hay suficientes unidades de {nombre_producto} en el inventario.")  
        else:
            # Imprimimos un mensaje de error si el producto no está en el inventario
            print(f"{nombre_producto} no está disponible en el inventario.")  

    # Definimos un método para calcular el precio total de los productos en el carrito
    def calcular_precio_total(self):  
        """
        Método para calcular el precio total de los productos en el carrito de compras.

        Parámetros:
        - Ninguno
        
        Retorna:
        - float: El precio total de los productos en el carrito.
        """
        # Calculamos la suma de los precios de todos los productos en el carrito
        precio_total = sum(producto.precio for producto in self.carrito)
        # Retornamos el precio total  
        return precio_total  
    
    # Definimos un método para procesar el pago de los productos en el carrito
    def pagar(self):
        """
        Método para procesar el pago de los productos en el carrito de compras.

        Retorna:
        - None
        """
        while True:
            try:
                # Obtenemos el monto a pagar
                monto = float(input("Ingrese el monto a pagar: "))
                # Calcula el precio total de los productos en el carrito de compras
                precio_total = self.calcular_precio_total()
                # Verifica si el monto ingresado es suficiente para pagar el total de la compra 
                if monto >= precio_total:
                    # Calcula el cambio  
                    cambio = monto - precio_total  
                    # Muestra un mensaje de confirmación del pago y el cambio con dos decimales
                    print(f"¡Pago exitoso! Su cambio es de {cambio:.2f}")
                    # Vacía el carrito después de realizar el pago  
                    self.carrito = []
                    break  # Sale del bucle si el pago fue exitoso
                else:
                    # Muestra un mensaje de error si el monto ingresado es insuficiente
                    print("El monto ingresado no es suficiente para pagar el total de la compra.")
                    # Continuará solicitando un nuevo monto
            except ValueError:
                # Muestra un mensaje de error si se ingresa un monto no válido
                print("Por favor, ingresa un monto válido.")


    # Define el método para ver la información detallada de un producto en el inventario
    def ver_producto(self, nombre_producto):  
        """
        Método para ver la información detallada de un producto en el inventario.

        Parámetros:5

        - nombre_producto (str): El nombre del producto que se desea ver.
        
        Retorna:
        - None
        """
        # Elimina los espacios en blanco al principio y al final del nombre y convierte a minúsculas
        nombre_producto = nombre_producto.strip().lower() 
        # Verifica si el producto está disponible en el inventario 
        if nombre_producto in self.inventario: 
            # Obtiene el producto del inventario 
            producto = self.inventario[nombre_producto]
             # Muestra la información detallada del producto  
            print(producto.info_libro()) 
        else:
            # Muestra un mensaje de error si el producto no está disponible en el inventario
            print("El producto no está en el inventario.")  


    # Define el método para ver el inventario completo
    def ver_inventario(self):  
        """
        Método para ver el inventario completo.

        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Muestra un encabezado indicando que se está mostrando el inventario
        print("Inventario:")
        # Recorre todos los productos en el inventario  
        for producto in self.inventario.values(): 
            # Muestra la información detallada de cada producto 
            print(producto.info_libro())  

    # Define el método para ver los productos en el carrito de compras
    def ver_carrito(self):  
        """
        Método para ver los productos en el carrito de compras.

        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Verifica si hay productos en el carrito de compras
        if self.carrito:  
            # Muestra un encabezado indicando que se están mostrando los productos en el carrito
            print("Productos en el carrito:")  
            # Recorre todos los productos en el carrito de compras
            for producto in self.carrito: 
                # Muestra el título de cada producto 
                print(producto.titulo) 
            # Muestra el precio total de los productos en el carrito con dos decimales 
            print(f"Precio total a pagar: {self.calcular_precio_total():.2f}")  
        else:
            # Muestra un mensaje indicando que el carrito de compras está vacío
            print("El carrito está vacío.")  


# Ejemplo de uso:

# Creación de instancia de ECommerce
ecommerce = ECommerce() 

# Ingreso de libros al inventario (simulado como trabajador)
# Crea un libro físico
libro1 = LibroFisico("La Comunidad del Anillo", "J.R.R Tolkien", 29.99, "Libro físico", "980 g")
# Solicita al usuario ingresar la cantidad de libros disponibles  
libro1.establecer_cantidad()  
# Agrega el libro al inventario de la tienda
ecommerce.agregar_al_inventario(libro1)  

# Crea un audiolibro
libro2 = AudioLibro("El codigo Da Vinci", "Dan Brown", 24.95, "Audio libro", 36000)
# Solicita al usuario ingresar la cantidad de audiolibros disponibles  
libro2.establecer_cantidad()  
# Agrega el audiolibro al inventario de la tienda
ecommerce.agregar_al_inventario(libro2)  

# Visualización del inventario (opcional)
print("Inventario actual:")
# Recorre todos los productos en el inventario
for producto in ecommerce.inventario.values(): 
    # Muestra la información detallada de cada producto en el inventario 
    print(producto.info_libro())  

# Simulación de la compra por parte de un cliente
print("\n¡Bienvenido a nuestra tienda en línea!")
while True:
    # Solicita al cliente que elija un producto o finalice la compra
    opcion = input("¿Qué producto deseas agregar al carrito? (Escribe 'fin' para pagar y salir): ") 
    # Verifica si el cliente ha decidido finalizar la compra 
    if opcion.lower() == "fin":  
        # Muestra los productos en el carrito de compras
        ecommerce.ver_carrito()  
        # Solicita al cliente ingresar el monto para realizar el pago
        
        # Procesa el pago de los productos en el carrito
        ecommerce.pagar() 
        # Sale del bucle mientras después de realizar el pago 
        break  
    else:
        # Agrega el producto seleccionado por el cliente al carrito de compras
        ecommerce.agregar_al_carrito(opcion)

# Muestra nuevamente los productos en el carrito de compras después de la compra
ecommerce.ver_carrito()  
# Muestra el inventario completo después de la compra
ecommerce.ver_inventario()  
