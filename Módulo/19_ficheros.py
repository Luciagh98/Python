try:
  fichero_lectura = open("Fichero_lectura.txt","r+")

  for line in fichero_lectura.readlines():
    print(line)
  
  line = fichero_lectura.readline()
  print(line)

  fichero_lectura.seek(0)
  fichero_escritura = open("Fichero_lectura.txt","w+")
  fichero_escritura.writelines(fichero_lectura.readlines())
  fichero_escritura.write("Otro texto\nOtro mas")

  """
  Read Only (r): solo lectura, falla si el fichero no existe, la posición (seek) es la cero.
  Read and Write (r+): lectura y escritura, falla si el fichero no existe. La posición (seek) es la cero.
  Write Only (w): Solo escritura, si el fichero no existe lo crea. Reemplaza el contenido. La posicion (seek) es de cero. 
  Write and Read (w+): Lectura y escritura, si el fichero no existe lo crea.Reemplaza el contenido. La posicion (seek) es de cero. 
  Append Only (a): Solo escritura, si el ficgro no existe lo crea. Reemplaza el contenido. La posicion (seek) es el final del fichero.
  Append and Read (a+): Lectra y escritura, si el fichero no existe lo crea. Reemplaza el contenido. La posicion (seek) es el final del fichero. 
  """

  fichero_lectura.close()
  fichero_escritura.close()
except Exception as ex:
  print(ex)
