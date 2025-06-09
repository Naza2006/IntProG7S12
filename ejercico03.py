#Calcular la suma de los dígitos de un número elevado a una potencia

def suma_digitos_potencia(base, exponente):
    resultado = base ** exponente
    suma = sum(int(d) for d in str(resultado))
    return suma