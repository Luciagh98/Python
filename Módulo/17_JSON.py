#El primer caso es la Codificación, convierte nuestros datos desde Python a JSON.

import json
# Crear un diccionario Python
datos_python = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ejemploville"
}
# Convertir el diccionario a una cadena JSON
json_string = json.dumps(datos_python)
print(json_string)

#Por otro lado, tenemos la Decodificación, que transforma los datos desde JSON a Python.
# Una cadena JSON de ejemplo
json_string = '{"nombre": "Juan", "edad": 30, "ciudad": "Ejemploville"}'
# Convertir la cadena JSON a un objeto de Python
datos_python = json.loads(json_string)
print(datos_python)

#Se puede dar el caso de tener archivos JSON, y no tener la necesidad de transformarlos. Para ello podemos leerlos json.load() o escribirlos json.dump().

# Escribir datos a un archivo JSON
with open('datos.json', 'w') as archivo_salida:
    json.dump(datos_python, archivo_salida)
# Leer datos desde un archivo JSON
with open('datos.json', 'r') as archivo_entrada:
    datos_leidos = json.load(archivo_entrada)
print(datos_leidos)

#____________________
import json
textojson = '{"nombre":"Juan","edad":36,"ciudad":"Madrid","coches": ["Seat","Audi"]}'

x = json.loads(textojson)

print(x['nombre'])
print(x['coches'][0])

y = [{
    "nombre":"Paco",
    "edad":40,
    "casado": True, 
    "mascotas":None, 
    "coches":[
        {"modelo":"BMW","color":"rojo"},
        {"modelo":"Audi","color":"blanco"}
    ]
}]

print(y[0]["coches"])

textojsony = json.dumps(y)
print(textojsony)
