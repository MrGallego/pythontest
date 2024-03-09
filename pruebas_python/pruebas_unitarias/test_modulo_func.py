import unittest
from pruebas_unitarias.modulo import sum, resta, multiplicacion, modulo_p, logaritmo_base_10, factorial

class TestModulo(unittest.TestCase):
    def test_sum(self):
        # Prueba para la función sum
        self.assertEqual(sum(2, 3), 5)

    def test_failed_sum(self):
        self.assertNotEqual(sum(2, 3), 6)
        
    def test_true_sum(self):
        self.assertTrue(sum(2, 3) == 5) 

    def test_resta(self):
        # Prueba para la función resta
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        # Prueba para la función multiplicacion
        self.assertEqual(multiplicacion(2, 3), 6)

    def test_modulo(self):
        # Prueba para la función modulo
        self.assertEqual(modulo_p(10, 3), 1)

    def test_logaritmo_base_10(self):
        # Prueba para la función logaritmo_base_10
        self.assertEqual(logaritmo_base_10(100), 2)

    def test_factorial(self):
        # Prueba para la función factorial
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()


