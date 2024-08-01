import os
# Obtén una lista de todos los archivos y directorios en el directorio actual
archivos = os.listdir('.')
for archivo in archivos:
    print(archivo)

#_______________
import os
for variable,valor in os.environ.items():
    print(f"{variable}: {valor}")

print(os.path.abspath("./18_sistema_operativo.py"))
print(os.path.isdir("./mimoduloavd"))
print(os.path.isfile("./mimoduloavd"))

print(os.path.getsize("./18_sistema_operativo.py"))
print(os.path.getmtime("./18_sistema_operativo.py"))

import datetime
x = datetime.datetime.fromtimestamp(os.path.getmtime("./18_sistema_operativo.py"))
print(x)