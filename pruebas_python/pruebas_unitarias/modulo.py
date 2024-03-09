import math

def sum(jcgg_a, jcgg_b):
    total = jcgg_a + jcgg_b
    return total

def resta(jcgg_a, jcgg_b):
    if isinstance(jcgg_a, str) and isinstance(jcgg_b, str):
        raise TypeError("La resta de caracteres no está definida")
    result = jcgg_a - jcgg_b
    return result

def multiplicacion(jcgg_a, jcgg_b):
    total = jcgg_a * jcgg_b
    return total

def modulo_p(jcgg_a, jcgg_b):
    total = jcgg_a % jcgg_b
    return total

def logaritmo_base_10(jcgg_numero):
    return math.log10(jcgg_numero)

def factorial(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado