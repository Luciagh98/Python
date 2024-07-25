#Listas
colores = ["rojo","amarillo","azul",4]#No hace falta que tenga el mismo tipo de dato
colores = colores + ["verde"] #Se añade automaticamente
print(colores)
print(colores[1])
print(colores[-1]) #Ultimo elemento
print(colores[:2]) #De dos en dos, etc.

#Conjuntos
conjunto = {1,2,3}#Elementos únicos
conjunto.add(4)

#Diccionarios
meses ={"Enero":1,"Febrero":2,"Marzo":3}
print(meses["Enero"])
meses["Abril"] = 4
print(meses)

#Tuplas
frutas = ("manzana","pera","cereza","cereza")#No mutables
frutas[1] ="kiwi" #Error
#Se utilizan cuando se definen ua funcion que puede retornar mas de un valor
#Para registros únicos