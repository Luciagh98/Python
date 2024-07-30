def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado = factorial(5)
print(resultado)

def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= 1
    return resultado

print("factorial(5)=", factorial(5)) #120 - 1*2*3*4*5

def factorialrecursivo(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorialrecursivo(numero-1)

print("factorialrecursivo(5)=", factorialrecursivo(5))

factoriallambda = lambda numero: 1 if numero == 1 else numero * factoriallambda(numero-1)
print("factoriallambda(5)= ", factoriallambda(5))

# 1, 1, 2, 3, 5, 8

def fibonacci(numero):
    if numero == 1  or numero == 2:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

print("fibonacci(7)=", fibonacci(7))

fibonaccilambda = lambda numero: 1 if numero==1 or numero==2 else fibonaccilambda(numero-1) + fibonaccilambda(numero-2)
print("fibonaccilambda(7)=", fibonaccilambda(7))