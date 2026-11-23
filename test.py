import unittest

from calculator import calculate, square, square_root


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, 5, "+"), 15)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 5, "-"), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10, 5, "*"), 50)

    def test_division(self):
        self.assertEqual(calculate(10, 5, "/"), 2)

    def test_modulus(self):
        self.assertEqual(calculate(10, 3, "%"), 1)

    def test_power(self):
        self.assertEqual(calculate(2, 3, "**"), 8)

    def test_square(self):
        self.assertEqual(square(5), 25)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            square_root(-25)


if __name__ == "__main__":
    unittest.main()