
import unittest
from src.roman_converter import decimal_to_roman  # Suponiendo que la función estará en roman_converter.py

class TestRomanConverter(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(9), "IX")

    def test_tens(self):
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_hundreds(self):
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_thousands(self):
        self.assertEqual(decimal_to_roman(1000), "M")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)

if __name__ == "__main__":
    unittest.main()