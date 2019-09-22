import unittest
import math_lib
import random
import statistics


# Testing none input
class TestNone(unittest.TestCase):

    def test_mean_none(self):
        self.assertEqual(math_lib.list_mean(None), None)

    def test_stdev_null(self):
        self.assertEqual(math_lib.list_stdev(None), None)

# Testing null input
class TestNull(unittest.TestCase):

    def test_mean_null(self):
        self.assertRaises(TypeError, lambda: math_lib.list_mean())

    def test_stdev_null(self):
        self.assertRaises(TypeError, lambda: math_lib.list_stdev())


# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def test_mean_string(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean(str('hi')))

    def test_stdev_string(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev(str('hi')))

    def test_mean_int(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean(4))

    def test_stdev_int(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev(4))

    def test_mean_float(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean(420.69))

    def test_stdev_float(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev(420.69))

    def test_mean_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_mean(True))

    def test_stdev_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: math_lib.list_stdev(True))

# Testing empty array input
class TestEmptyArray(unittest.TestCase):

    def test_mean_empty_array(self):
        self.assertEqual(math_lib.list_mean([]), None)

    def test_stdev_empty_array(self):
        self.assertEqual(math_lib.list_stdev([]), None)

# Testing ones array input
class TestOnesArray(unittest.TestCase):

    def test_mean_ones_array(self):
        self.assertEqual(math_lib.list_mean([1, 1, 1, 1]), 1)

    def test_stdev_ones_array(self):
        self.assertEqual(math_lib.list_stdev([1, 1, 1, 1]), 0)

# Testing looped random array input
class TestRandomIntArray(unittest.TestCase):

    def test_mean_random_int_array(self):
        for i in range(100):
            A = []
            for i in range(100):
                A.append(random.randint(1, 100))
            self.assertEqual(round(math_lib.list_mean(A), 5),
                             round(statistics.mean(A), 5))

    def test_stdev_random_int_array(self):
        for i in range(100):
            A = []
            for i in range(100):
                A.append(random.randint(1, 100))
            self.assertEqual(round(math_lib.list_stdev(A), 5),
                             round(statistics.pstdev(A, statistics.mean(A)), 5))

class TestRandomFloatArray(unittest.TestCase):

    def test_mean_random_float_array(self):
        for i in range(100):
            A = []
            for i in range(100):
                A.append(random.uniform(1, 100))
            self.assertEqual(round(math_lib.list_mean(A), 5),
                             round(statistics.mean(A), 5))

    def test_stdev_random_float_array(self):
        for i in range(100):
            A = []
            for i in range(100):
                A.append(random.uniform(1, 100))
            self.assertEqual(round(math_lib.list_stdev(A), 5),
                             round(statistics.pstdev(A, statistics.mean(A)), 5))


if __name__ == '__main__':
    unittest.main()