import unittest
from sci_cal import square_root

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-1), "Imaginary roots")


if __name__ == "__main__":
    unittest.main()
