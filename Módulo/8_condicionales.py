x = 5

if x < 5:
  print("El numero es menor que 5")
else:
  print("El numero no es menor que 5")

if x < 5:
  print("El numero es menor que 5")
else:
  if x > 5:
    print("El numero es mayor que 5")
  else:
    print("El numero es 5")

if x < 5:
  print("El numero es menor que 5")
elif x > 5:
  print("El numero es mayor que 5")
elif x > 5:
  print("El numero es mayor que 5")
else:
  print("El numero es 5")

# if en una unica lina
y = "El numero es menor que 5" if x < 5 else "el numero no es menor que 5"
print(y)

y = "el numero es menor que 5" if x < 5 else ("el numero es mayor que 50" if x > 5 else "el numero es 5")
print(y)