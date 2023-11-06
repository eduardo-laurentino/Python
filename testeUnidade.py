import unittest

def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma_positiva(self):
        resultado = soma(3, 5)
        self.assertEqual(resultado, 8)

    def test_soma_negativa(self):
        resultado = soma(-2, -7)
        self.assertEqual(resultado, -9)

if __name__ == '__main__':
    unittest.main()