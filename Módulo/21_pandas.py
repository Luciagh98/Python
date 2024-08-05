import pandas as pd

# Crear un DataFrame a partir de un diccionario
data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35],
        'Ciudad': ['A', 'B', 'C']}

df = pd.DataFrame(data)

# Seleccionar columnas por nombre
ages = df['Edad']

# Filtrar filas basadas en una condición
young_people = df[df['Edad'] < 30]

#_____________
rrss= [
  {"Nombre":"Facebook","Cantidad":2449,"Es_FBK":True,"Año":2006},
  {"Nombre":"Twitter","Cantidad":339,"Es_FBK":False,"Año":2006},
  {"Nombre":"Instagram","Cantidad":2000,"Es_FBK":True,"Año":2018},
  {"Nombre":"Youtube","Cantidad":663,"Es_FBK":False,"Año":2005},
  {"Nombre":"Linkedin","Cantidad":100,"Es_FBK":False,"Año":2003},
  {"Nombre":"WhatsApp","Cantidad":1600,"Es_FBK":True,"Año":2009}
]

df = pd.DataFrame(rrss)

print(df)
print(df.head(2))

print(df.loc[1])
print(df.iloc[1,0])

print(df[["Nombre"]])
print(df[["Nombre","Cantidad"]])

print(df["Cantidad"] > 1500)
print(df[df["Cantidad"] > 1500])

print(df.dtypes)
