import random

# Constantes
TABLERO_TAMANIO = 10
BARCOS_TAMANIOS = [2, 3, 3, 4, 5]
AGUA = "~"
BARCO = "B"
HUNDIDO = "X"
DISPARO_AGUA = "O"

def crear_tablero():
  return [[AGUA for _ in range(TABLERO_TAMANIO)] for _ in range(TABLERO_TAMANIO)]

def imprimir_tablero(tablero, ocultar_barcos=True):
  print(" " + " ".join(str(i) for i in range(TABLERO_TAMANIO)))
  for i in range(TABLERO_TAMANIO):
    fila = [str(i)]
    for j in range(TABLERO_TAMANIO):
      if ocultar_barcos and tablero[i][j] == BARCO:
        fila.append(AGUA)
      else:
        fila.append(tablero[i][j])
    print(" ".join(fila))

def colocar_barcos(tablero):
  for tam in BARCOS_TAMANIOS:
    while True:
      fila = random.randint(0, TABLERO_TAMANIO - 1)
      columna = random.randint(0, TABLERO_TAMANIO - 1)
      direccion = random.choice(["horizontal", "vertical"])
      if es_posicion_valida(tablero, fila, columna, tam, direccion):
        colocar_barco(tablero, fila, columna, tam, direccion)
        break

def es_posicion_valida(tablero, fila, columna, tam, direccion):
    if direccion == "horizontal":
      if columna + tam > TABLERO_TAMANIO:
        return False
      return all(tablero[fila][columna + i] == AGUA for i in range(tam))
    elif direccion == "vertical":
        if fila + tam > TABLERO_TAMANIO:
          return False
        return all(tablero[fila + i][columna] == AGUA for i in range(tam))
    
def colocar_barco(tablero, fila, columna, tam, direccion):
    if direccion == "horizontal":
      for i in range(tam):
          tablero[fila][columna + i] = BARCO
    elif direccion == "vertical":
      for i in range(tam):
          tablero[fila + i][columna] = BARCO

def disparar(tablero, fila, columna):
  if tablero[fila][columna] == BARCO:
    tablero[fila][columna] = HUNDIDO
    return True
  elif tablero[fila][columna] == AGUA:
    tablero[fila][columna] = DISPARO_AGUA
  return False

def hundir_la_flota():
  tablero = crear_tablero()
  colocar_barcos(tablero)
  while True:
    imprimir_tablero(tablero)
    try:
        fila = int(input("Ingresa la fila para disparar: "))
        columna = int(input("Ingresa la columna para disparar: "))
        if fila < 0 or fila >= TABLERO_TAMANIO or columna < 0 or columna>= TABLERO_TAMANIO:
          print("Posición fuera del tablero. Inténtalo de nuevo.")
          continue
        if disparar(tablero, fila, columna):
          print("¡Barco golpeado!")
        else:
          print("¡Disparo al agua!")
        if all(all(casilla != BARCO for casilla in fila) for fila in tablero):
          imprimir_tablero(tablero, ocultar_barcos=False)
          print("¡Felicidades! Has hundido la flota.")
          break
    except ValueError:
      print("Entrada inválida. Ingresa un número válido.")

if __name__ == "__main__":
  hundir_la_flota()