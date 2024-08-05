import numpy as np

lista = [1,2,3]
nplista = np.array(lista)

print(nplista)

print(np.arange(0,5))
print(np.zeros(5))
print(np.ones(5))

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape)

arr = np.array([0,1,2,3,4,5])
print(arr.reshape(2,3))

print(matriz + 2)

print(arr + arr)

copiar_arr = arr.copy()
print(arr.max())
print(arr.min())
print(arr.sum())

for item in arr:
  print(item)