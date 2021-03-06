import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_power(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_modulus(self):
        result = rpn.calculate("7 2 %")
        self.assertEqual(1, result)
    def test_intDivision(self):
        result = rpn.calculate("7 2 //")
        self.assertEqual(3, result)
    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
    def test_repeat(self):
        result = rpn.calculate("4 2 6 * &")
        self.assertEqual(48, result)

    
    
