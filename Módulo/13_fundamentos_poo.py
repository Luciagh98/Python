# Definición de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Creación de un objeto de la clase Persona
persona1 = Persona("Juan", 30)
print(persona1.presentarse())  # Output: Hola, mi nombre es Juan y tengo 30 años.

# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo): # Abstracción (Método constructor de clase)
        self.marca = marca # Atributos
        self.modelo = modelo

# Clase hija
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo) # Herencia (Se llama a super() recibiendo Vehículo)
        self.color = color


class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self): # Polimorfismo(Se redefine un método de la superclase, cambiando su comportamiento)
        return "Guau Guau"

class Gato(Animal):
    def sonido(self): # Polimorfismo
        return "Miau Miau"
    
#--------------

class Persona:
    """ Esta clase define los atributos de persoa"""
    def __init__(self, nombre, edad):
        """
        Constructor de la persona
        Args:
            nombre(str): Nombre de la persona
            edad(int): edad en años de la persona
            """
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print("Hola", self.nombre)

    def saludo_estatico():
        print("Hola a todos")

    def __repr__(self): #Representación
        return repr((self.nombre, self.edad))

    def __str__(self): #Representacíón en un string
        return f"La persona se llama {self.nombre} tiene {self.edad} años."
        

x = Persona("Juan",30)

print("x.nombre",x.nombre)
print("x.edad",x.edad)
x.saludo()

Persona.saludo(x)
Persona.saludo_estatico()

print(x)
print(repr(x)) #Tomará valors distintos seguns la persona
print(str(x)) #Más endendible a la mayoria



