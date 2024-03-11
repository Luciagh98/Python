def imprimir_tablero(tablero):
  for fila in tablero:
    print(" | ".join(fila))
    print("-" * 9)

def comprobar_ganador(tablero, jugador):
  for i in range(3):
    if all(tablero[i][j] == jugador for j in range(3)) or \
      all(tablero[j][i] == jugador for j in range(3)):
        return True
    
    if all(tablero[i][i] == jugador for i in range(3)) or \
      all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False
  
def is_tablero_full(tablero):
  return all(all(casilla != " " for casilla in fila) for fila in tablero)

def tres_en_linea():
  tablero = [[" " for _ in range(3)] for _ in range(3)]
  jugador_actual = "X"

  print("¡Bienvenido al Tres en línea!")
  imprimir_tablero(tablero)

  while True:
      print(f"Turno de jugador {jugador_actual}")
      fila = int(input("Fila (0, 1, 2): "))
      col = int(input("Columna (0, 1, 2): "))
      
      if tablero[fila][col] == " ":
          tablero[fila][col] = jugador_actual
          imprimir_tablero(tablero)

          if comprobar_ganador(tablero, jugador_actual):
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break
          elif is_tablero_full(tablero):
            print("¡Empate!")
            break

          jugador_actual = "O" if jugador_actual == "X" else "X"
      else:
        print("Esa casilla ya está ocupada. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
     tres_en_linea()