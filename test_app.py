import unittest
from sample import sumar, restar, multiplicar, dividir

class TestApp(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 4), 7)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()