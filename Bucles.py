#nos permiten iterar sobre unos valores, mostrando lo que deseamos.

nombres = ["David","Lucia","Arnedo","Garcia",5]

for elemento in nombres:
  print(elemento)

#nos imprime los elementos en filas, "quitandolo" de la lista.
  
nombres = ["David","Lucia","Arnedo","Garcia",5]
position = 1

for elemento in nombres:
  print(position)
  position += 1
  print(elemento)