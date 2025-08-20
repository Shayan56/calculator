# test_calculator.py
import unittest
from shayan import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(10, self.calc.add(3, 6))

    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3))

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6))

    def test_divide(self):
        self.assertEqual(3, self.calc.divide(6, 2))

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
