def suma_digitos_potencia(base, exponente):
    resultado = base ** exponente
    suma = sum(int(d) for d in str(resultado))
    return suma