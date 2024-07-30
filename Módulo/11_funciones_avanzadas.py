def sumados (a, b=2):
  return a + b

print("sumados(a, b) = ", sumados(4))
print("sumados(a, b) = ", sumados(4,3))

print("sumados(a, b) = ", sumados(b=2, a=1))

def sumarvarios(a,*args):
  result = 0
  for item in args:
    result += item
  return a - result

print("sumarvarios(1, 3, 4, 5) = ", sumarvarios(1,3,4,5))

def connombre(**kwargs):
  print("kwargs", kwargs)
  return kwargs.get('a') + kwargs.get('b')

print("connombre(a=5, b=6, c=5)=", connombre(a=5, b=6, c= 5))