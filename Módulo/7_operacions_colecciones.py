print(len("Hola Mundo"))
print(len(["Hola", "Mundo"]))

frutas = ["platano","coco","naraja"]
frutas = frutas + ["kiwi","manzana"]
print(frutas)

print(frutas.index("coco"))
frutas.append("naranja")
print(frutas)

frutas.insert(1,"naranja")
print(frutas)

frutas.extend(["otro"])
print(frutas)

lista = [1,7,5,4,12,3]
lista.sort() #de menor a mayor
print(lista)
lista.sort(reverse=True) #de mayor a menor
print(lista)

lista = [1,7,5,4,12,3]
lista = sorted(lista) #Alternativa
print(lista)

lista = sorted(lista, reverse=True) #Alternativa
print(lista)

#Operacions conjuntos
c1 ={1,2,3,4,5,6}
c2 = {2,4,6,8,10}

print(c1 | c2)
print(c1.union(c2)) #Unión

print(c1 & c2)
print(c1.intersection(c2))

print(c1-c2)
print(c1.difference(c2))

print(c1 ^c2)
print(c1.symmetric_difference(c2))

#Diccionarios
meses = {"Enero":1,"Febrero":2,"Marzo":3}

for key in meses:
  print(key, meses[key])

print(meses.keys())
print(meses.values())
print(meses.items())

print(meses["Enero"])
#print(meses["Abril"]) -- ERROR
print(meses.get("Abril")) #None si no exist. Para evitar errores

print("Enero" in meses.keys())
print("Abril" in meses.keys())


