#
# @Author Juan Camilo Gonzalez Gallego
# @date 2024/02/20
# @description test unit for functions that maths
import pytest
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

def modulo(jcgg_a, jcgg_b):
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

#####################################################################################


def test_sum():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 4
    jcgg_input_b = 9
    jcgg_expected_result = 13  # Un resultado correcto 

    # Act: Llamar a la función que estamos probando
    result = sum(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result == jcgg_expected_result, f"La suma de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_sum_failed():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 4
    jcgg_input_b = 9
    jcgg_expected_result = 14  # Un resultado incorrecto a propósito

    # Act: Llamar a la función que estamos probando
    result = sum(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result != jcgg_expected_result, f"La suma de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_sum_passed_result_decimal():
    # Arrange: preparacion de datos de prueba
    jcgg_input_a = 3.5
    jcgg_input_b = 4.9
    jcgg_expected_result = 8.4

    # Act: Llamar a la función que estamos probando
    result = sum(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result == jcgg_expected_result, f"La suma de {jcgg_input_a} y {jcgg_input_b} es correcta = {jcgg_expected_result}"

def test_sum_passed_character():

    # Arrange: preparacion de datos de prueba
    jcgg_input_a = 'a'
    jcgg_input_b = 'b'
    jcgg_expected_result = 'ab'

    # Act: Llamar a la función que estamos probando
    result = sum(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result == jcgg_expected_result, f"La concatenación de {jcgg_input_a} y {jcgg_input_b} es correcta = {jcgg_expected_result}"


######################################################################################################################################## 

def test_resta():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 9
    jcgg_input_b = 4
    jcgg_expected_result = 5  # Un resultado correcto 

    # Act: Llamar a la función que estamos probando
    result = resta(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result == jcgg_expected_result, f"La resta de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_resta_failed():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 4
    jcgg_input_b = 9
    jcgg_expected_result = -4  # Un resultado incorrecto a propósito

    # Act: Llamar a la función que estamos probando
    result = resta(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert result != jcgg_expected_result, f"La resta de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_resta_passed_result_decimal():
    # Arrange: preparacion de datos de prueba
    jcgg_input_a = 10.5
    jcgg_input_b = 3.5
    jcgg_expected_result = 7.0

    # Act: Llamar a la función que estamos probando
    result = resta(jcgg_input_a, jcgg_input_b)

    assert result == jcgg_expected_result, f"La resta de {jcgg_input_a} y {jcgg_input_b} es correcta = {jcgg_expected_result}"

def test_resta_character_raises_error():
    jcgg_input_a = 'b'
    jcgg_input_b = 'a'

    with pytest.raises(TypeError):
        resta(jcgg_input_a, jcgg_input_b)

################################################################################################
        
def test_multiplicacion():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 4
    jcgg_input_b = 9
    jcgg_expected_result = 36  # El resultado de la multiplicación

    # Act: Llamar a la función que estamos probando
    jcgg_result = multiplicacion(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"La multiplicación de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_multiplicacion_failed():
    # Arrange: Configuración inicial, preparación de datos
    jcgg_input_a = 4
    jcgg_input_b = 9
    jcgg_expected_result = 40  # Un resultado incorrecto a propósito

    # Act: Llamar a la función que estamos probando
    jcgg_result = multiplicacion(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert jcgg_result != jcgg_expected_result, f"La multiplicación de {jcgg_input_a} y {jcgg_input_b} no debería ser {jcgg_expected_result}"

def test_multiplicacion_result_decimal():
    # Arrange: preparacion de datos de prueba
    jcgg_input_a = 3.5
    jcgg_input_b = 4.9
    jcgg_expected_result = 17.15

    # Act: Llamar a la función que estamos probando
    jcgg_result = multiplicacion(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado con una tolerancia
    assert abs(jcgg_result - jcgg_expected_result) < 0.0001, f"La multiplicación de {jcgg_input_a} y {jcgg_input_b} es correcta = {jcgg_expected_result}"

def test_multiplicacion_caracteres():
    # Prueba de multiplicación de un carácter por un número entero
    jcgg_caracter = 'a'
    jcgg_multiplicado = jcgg_caracter * 3
    assert jcgg_multiplicado == 'aaa', "La multiplicación de caracteres no funciona como se espera"

def test_error_multiplicacion_caracteres():
    # Prueba para verificar que intentar multiplicar dos caracteres directamente genere un error
    with pytest.raises(TypeError):
        jcgg_resultado = 'a' * 'b'

#####################################################################################################################
        
def test_modulo_integer():
    # Arrange: Preparación de datos de prueba
    jcgg_input_a = 10
    jcgg_input_b = 3
    jcgg_expected_result = 1

    # Act: Llamar a la función que estamos probando
    jcgg_result = modulo(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"El módulo de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_modulo_zero():
    # Arrange: Preparación de datos de prueba
    jcgg_input_a = 10
    jcgg_input_b = 1
    jcgg_expected_result = 0

    # Act: Llamar a la función que estamos probando
    jcgg_result = modulo(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"El módulo de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_modulo_negative():
    # Arrange: Preparación de datos de prueba
    jcgg_input_a = -10
    jcgg_input_b = 3
    jcgg_expected_result = 2  # El módulo de -10 dividido por 3 es 2

    # Act: Llamar a la función que estamos probando
    jcgg_result = modulo(jcgg_input_a, jcgg_input_b)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"El módulo de {jcgg_input_a} y {jcgg_input_b} debería ser {jcgg_expected_result}"

def test_error_modulo_caracteres():
    # Prueba para verificar que intentar multiplicar dos caracteres directamente genere un error
    with pytest.raises(TypeError):
        jcgg_resultado = 'a' % 'b'        


#####################################################################################################################

def test_logaritmo_base_10_integer():
    # Arrange: Preparación de datos de prueba
    jcgg_numero = 100
    jcgg_expected_result = 2.0

    # Act: Llamar a la función que estamos probando
    jcgg_result = logaritmo_base_10(jcgg_numero)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"El logaritmo en base 10 de {jcgg_numero} debería ser {jcgg_expected_result}"

def test_logaritmo_base_10_decimal():
    # Arrange: Preparación de datos de prueba
    jcgg_numero = 10.0
    jcgg_expected_result = 1.0

    # Act: Llamar a la función que estamos probando
    jcgg_result = logaritmo_base_10(jcgg_numero)

    # Assert: Verificar el resultado esperado
    assert jcgg_result == jcgg_expected_result, f"El logaritmo en base 10 de {jcgg_numero} debería ser {jcgg_expected_result}"

def test_logaritmo_base_10_zero():
    # Arrange: Preparación de datos de prueba
    jcgg_numero = 0
    # Act y Assert: Verificar que se lance una excepción al calcular el logaritmo de cero
    with pytest.raises(ValueError):
        logaritmo_base_10(jcgg_numero)

def test_error_logaritmo_base_10_caracteres():

    # Arrange: Preparación de datos de prueba
    jcgg_numero = 'k'
    # Prueba para verificar que intentar multiplicar dos caracteres directamente genere un error
    with pytest.raises(TypeError):
        logaritmo_base_10(jcgg_numero)

###########################################################################################################################
        
def test_factorial_positivo():
    # Arrange: Preparación de datos de prueba
    numero = 5
    resultado_esperado = 120  # El factorial de 5 es 5*4*3*2*1 = 120

    # Act: Llamar a la función que estamos probando
    resultado = factorial(numero)

    # Assert: Verificar el resultado esperado
    assert resultado == resultado_esperado, f"El factorial de {numero} debería ser {resultado_esperado}"

def test_factorial_cero():
    # Arrange: Preparación de datos de prueba
    numero = 0
    resultado_esperado = 1  # El factorial de 0 es 1

    # Act: Llamar a la función que estamos probando
    resultado = factorial(numero)

    # Assert: Verificar el resultado esperado
    assert resultado == resultado_esperado, f"El factorial de {numero} debería ser {resultado_esperado}"

def test_factorial_negativo():
    # Arrange: Preparación de datos de prueba
    numero = -5

    # Act y Assert: Verificar que se levante una excepción para números negativos
    with pytest.raises(ValueError):
        factorial(numero)

def test_factorial_caracter():
    # Arrange: Preparación de datos de prueba
    numero = 'r'

    # Act y Assert: Verificar que se levante una excepción para caracteres
    with pytest.raises(TypeError):
        factorial(numero)