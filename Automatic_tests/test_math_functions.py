# Plik: test_math_functions.py

## aby urychomić ->python -m unittest test_math_functions.py
import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        """Test dodawania kilku dodatnich liczb."""
        self.assertEqual(add(1, 2, 3), 6)      # 1 + 2 + 3 = 6
        self.assertEqual(add(10, 20, 30), 60)  # 10 + 20 + 30 = 60

    def test_add_negative_numbers(self):
        """Test dodawania liczb ujemnych."""
        self.assertEqual(add(-1, -2, -3), -6)  # -1 + -2 + -3 = -6

    def test_add_mixed_numbers(self):
        """Test dodawania liczb dodatnich i ujemnych."""
        self.assertEqual(add(-1, 5, -2, 3), 5) # -1 + 5 + -2 + 3 = 5

    def test_add_no_arguments(self):
        """Test gdy funkcja add nie otrzymuje żadnych argumentów."""
        self.assertEqual(add(), 0)             # Suma pustego zestawu argumentów to 0

if __name__ == "__main__":
    unittest.main()
