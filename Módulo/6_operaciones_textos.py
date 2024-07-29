print(len("Hola Mundo"))

print("Hola Mundo".lower())
print("Hola Mundo".upper())
print("hola mundo".capitalize())

print("Hola Mundo".islower())
print("Hola Mundo".isupper())

palabras = ["Es","un","texto","de","prueba"]
print(" ".join(palabras))
print(",".join(palabras))

texto = "Es un, texto de, prueba"
print(texto.split(","))

texto = "Es un texto"+ " " + "de prueba"
print(texto)

texto= "Hola Mundo"
print(texto.replace("Hola","Adios"))

print("Mundo" in "Hola Mundo")
print("Hola Mundo".find("Mundo"))

print("Hola \"mundo\"")

x = 50
texto = f"La variable es igual a {x}."
print(texto)

texto = "La variable es igual a {:}".format(x)
print(texto)

y = 50.555
texto = "La variable es igual a {:2f}".format(y)
print(texto)