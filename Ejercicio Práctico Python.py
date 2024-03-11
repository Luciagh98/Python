def sumar(x, y):
  return x + y

def restar(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
 if y != 0:
    return x / y
 else:
    return "¡División entre cero no permitida!"

def potencia(x, y):
  return x ** y

def raiz_cuadrada(x):
  if x >= 0:
      return x ** 0.5
  else:
      return "No se puede calcular la raíz cuadrada de un número negativo"

def calculadora():
  print("¡Bienvenido a la Calculadora!")
  while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Salir")

    eleccion = input("Selecciona una opción (1/2/3/4/5/6/7): ")

    if eleccion == '7':
      print("¡Hasta luego!")
      break

    if eleccion in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Ingresa el primer número: "))

    if eleccion!= '6':
      num2 = float(input("Ingresa el segundo número: "))

    if eleccion == '1':
      print("Resultado:", sumar(num1, num2))
    elif eleccion == '2':
      print("Resultado:", restar(num1, num2))
    elif eleccion == '3':
      print("Resultado:", multiplicar(num1, num2))
    elif eleccion == '4':
      print("Resultado:", dividir(num1, num2))
    elif eleccion == '5':
      print("Resultado:", potencia(num1, num2))
    elif eleccion == '6':
      print("Resultado:", raiz_cuadrada(num1))
    else:
      print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
  calculadora()