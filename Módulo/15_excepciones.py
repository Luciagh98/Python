a = 5
b = 1

try:
    resultado = a/b
    print(resultado)
except TypeError:
    print("El tipo es incorrecto")
except (ZeroDivisionError,TypeError):
    print("O bien se está dividiento por cero o el tipo es incorrecto")
except Exception as excepcion:
    print("Error desconocido",excepcion)
finally:
    print("Codigo al finalizar con erorr o sin error")

class InvalidAgeException(Exception):
    """Esta excepcion se genera cuando la edad es menor que 18"""
    pass

def conducir_coche(edad):
    if edad < 18:
          raise InvalidAgeException
    else:
        print("Conducir coche")

print("conducir_coche(5)= ", conducir_coche(5))
print("conducir_coche(19)= ", conducir_coche(19))
