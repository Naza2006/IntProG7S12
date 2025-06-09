# Calcular el factorial de un número

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado