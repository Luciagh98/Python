#HERENCIA MULTIPLE
from typing import Any


class Base1:
  pass
class Base2:
  pass
class MultiDerived(Base1, Base2):
  pass

#Métodos mágicos
class Ejemplo:
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f"Ejemplo({self.valor})"
    def __add__(self, otro):
        return Ejemplo(self.valor + otro.valor)

#__iter__ 
class MiIterable:
    def __init__(self, maximo):
        self.maximo = maximo
    def __iter__(self):
        self.contador = 0
        return self
    def __next__(self):
        if self.contador < self.maximo:
          valor = self.contador
          self.contador += 1
          return valor
        else:
            raise StopIteration

#c__call__ 
class MiClase:
    def __init__(self):
        print("Se ha creado una instancia de MiClase.")
    def __call__(self, *args, **kwargs):
        print("Se ha llamado a la instancia de MiClase.")
mi_objeto = MiClase()  # Output: Se ha creado una instancia de MiClase.
mi_objeto()  # Output: Se ha llamado a la instancia de MiClase.

def mi_decorador(func):
    def envoltura():
        print("Algo antes de la función original.")
        func()
        print("Algo después de la función original.")
    return envoltura

@mi_decorador
def saluda():
    print("¡Hola!")

#Metaclases
class MiMeta(type):
    pass
class MiClase(metaclass=MiMeta):
    pass

#__________________________
class MediaAcumulada:
    def __init__(self):
        self.data = []
    def __call__(self, nuevo_valor):
        self.data.append(nuevo_valor)
        return sum(self.data)/len(self.data)

media_acumulada = MediaAcumulada()
print("media_acumulada(5)", media_acumulada(5))
print("media_acumulada(3)", media_acumulada(3))
print("media_acumulada(1)", media_acumulada(1))

print("media_aumulada.data",media_acumulada.data)

class Reverse:
    def __init__(self,data) -> None:
        self.data = data

    def __iter__(self):
        print("iter")
        self.index = len(self.data)
        return self
  
    def __next__(self):
        print("next")
        if self.index == 0:
          raise StopIteration
        self.index -= 1
        return self.data[self.index]

lista = Reverse([1,2,3,4,5])

for i in lista:
    print(i)

