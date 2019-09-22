import unittest
import math_lib


# Testing null input
class TestNullArray(unittest.TestCase):

    def test_mean_null_array(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean())

    def test_stdev_null_array(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev())

# Testing empty array input
class TestEmptyArray(unittest.TestCase):

    def test_mean_empty_array(self):
        self.assertRaises(ZeroDivisionError,
                          lambda: math_lib.list_mean([]))

    def test_stdev_empty_array(self):
        self.assertRaises(ZeroDivisionError,
                          lambda: math_lib.list_stdev([]))


if __name__ == '__main__':
    unittest.main()