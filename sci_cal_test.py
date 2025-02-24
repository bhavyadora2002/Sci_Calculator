import unittest
from sci_cal import square_root,factorial,power,log

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-1), "Imaginary roots")
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-1), "Enter positive number")
    def test_power(self):
        self.assertEqual(power(0,0), 1)
        self.assertEqual(power(1,39), 1)
        self.assertEqual(power(2,0), 1)
        self.assertEqual(power(-2,3), -8)
    def test_log(self):
        self.assertEqual(log(1), 1)
        self.assertEqual(log(0), "Undefined")
        self.assertEqual(log(-1), "Unknown")  

if __name__ == "__main__":
    unittest.main()
