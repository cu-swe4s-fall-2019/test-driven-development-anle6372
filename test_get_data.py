"""Unittesting framework for get_data.py

Parameters
----------
None

Returns
-------
None
"""

import get_data
import unittest
import random


# Testing none input
class TestNoneColumn(unittest.TestCase):

    def test_get_data_col_num_none(self):
        self.assertEqual(get_data.read_stdin_col(None), None)


# Testing null input
class TestNullColumn(unittest.TestCase):

    def test_get_data_col_num_null(self):
        self.assertRaises(TypeError, lambda: get_data.read_stdin_col())


# Testing incorrect input types
class TestIncorrectColumnInput(unittest.TestCase):

    def test_get_data_col_num_string(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(str('hi')))

    def test_get_data_col_num_float(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(420.69))

    def test_get_data_col_num_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(True))


class TestCorrectColumnInput(unittest.TestCase):

    # Testing correct constant
    def test_get_data_col_num_constant(self):
        self.assertEqual(get_data.read_stdin_col(5), 5)

    # Testing variable constant
    def test_get_data_col_num_variable(self):
        A = random.randint(1, 100)
        self.assertEqual(get_data.read_stdin_col(A), A)

    # Testing variable column number loop
    def test_get_data_col_num_variable_loop(self):
        for i in range(100):
            A = random.randint(1, 100)
            self.assertEqual(get_data.read_stdin_col(A), A)


if __name__ == '__main__':
    unittest.main()
