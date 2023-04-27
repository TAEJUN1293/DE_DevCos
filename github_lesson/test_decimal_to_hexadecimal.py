import unittest
from decimal_to_hexadecimal import decimal_to_hexadecimal

class TestDecimalToHexadecimal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_to_hexadecimal(10), "A")
        self.assertEqual(decimal_to_hexadecimal(255), "FF")
        self.assertEqual(decimal_to_hexadecimal(4096), "1000")
    
    def test_zero(self):
        self.assertEqual(decimal_to_hexadecimal(0), "0")
        
    def test_negative_numbers(self):
        self.assertEqual(decimal_to_hexadecimal(-10), "-A")
        self.assertEqual(decimal_to_hexadecimal(-255), "-FF")
        self.assertEqual(decimal_to_hexadecimal(-4096), "-1000")

if __name__ == '__main__':
    unittest.main()
