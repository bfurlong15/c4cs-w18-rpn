import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_factorial(self):
    	result = rpn.calculate("4 !")
    	self.assertEqual(24, result)
    def test_sin(self):
    	result = rpn.calculate("0 sin")
    	self.assertEqual(0, result)
    def test_cos(self):
    	result = rpn.calculate("0 cos")
    	self.assertEqual(1, result)
    def test_tan(self):
    	result = rpn.calculate("0 tan")
    	self.assertEqual(0, result)
    def test_copy(self):
    	result = rpn.calculate("5 6 3 copy")
    	self.assertEqual(4, result)
    def test_carat(self):
    	result = rpn.calculate("4 2 ^")
    	self.assertEqual(16, result)
