for i in range(1,6):
  print(i)

for i in ["rojo","amarillo","azul"]:
  print(i)
  print("otro print")

for index,item in enumerate(["rojo","amarillo","azul"]):
  print(index,item)

#for en una linea
[print(i) for i in ["rojo","amarillo","azul"]]

milista = [i*2 for i in range(5)]
print(milista)

milista = list(range(5))
print(milista)

x = 0
while x < 5:
  print(x)
  x += 1 #x = x + 1 x++

for i in range(5):
  if i == 3:
    break #ponerle fin al bucle
  elif i == 2:
    continue #evita es el codigo que existe debajo
  else:
    pass #no hace nada
  print(i)

print("Salir")
