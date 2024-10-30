import unittest
from calculadora_cientifica import basico, avancado

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basico.soma(2, 3), 5)

    def test_power(self):
        self.assertEqual(avancado.potencia(2, 3), 8)

if __name__ == "__main__":
    unittest.main()
