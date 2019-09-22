import unittest
import math_lib

class TestNullArray(unittest.TestCase):

    def test_mean_null_array(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean())

    def test_stdev_null_array(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev())

if __name__ == '__main__':
    unittest.main()