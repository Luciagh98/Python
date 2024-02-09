#Saber donde se declaran las variables, donde se usan....

variable_global = "Soy Global" #esta a primer nivel, ya que esta declarada en ámbito global

def probar_scope():
  variable_local= "Soy Local" #esta variable solo se usa dentro de la función
  print(variable_local)
  print(variable_global) 

probar_scope() #nos imprime las variables por el orden de dentro de la función

#print(variable_local) #el editor ya no la contempla fuera de la función, a su vez, nos dice que no existe fuera de la función. ERROR

def probar_scope():
  variable_local= "Soy Local"
  print(variable_local)
  print(variable_global)
  variable_global = "Soy Global des de otro scope"
  print(variable_global)

probar_scope() #Nos da error al intentar modificar la función global dentro de la función local

def probar_scope():
  variable_local= "Soy Local"
  print(variable_local)
  variable_global = "Soy Global des de otro scope"
  print(variable_global)

probar_scope()

#Al eliminar la primera impresión del global, ya va directo al de modificar. Por tanto, no busca la global dentro de la función, sinó que la modifica. 