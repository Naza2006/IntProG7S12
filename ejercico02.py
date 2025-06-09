#Convertir un número decimal a binario

def decimal_a_binario(n):
    if n <= 0:
        raise ValueError("El número debe ser un entero positivo.")
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario