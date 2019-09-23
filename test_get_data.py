import get_data
import unittest

# Testing none input
class TestNone(unittest.TestCase):

    def test_get_data_none(self):
        self.assertEqual(get_data.read_stdin_col(None), None)

# Testing null input
class TestNull(unittest.TestCase):

    def test_get_data_null(self):
        self.assertRaises(TypeError, lambda: get_data.read_stdin_col())


# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def test_get_data_string(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(str('hi')))

    def test_get_data_float(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(420.69))

    def test_get_data_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: get_data.read_stdin_col(True))

# Testing correct constant

    def test_get_data_constant(self):
        self.assertEqual(get_data.read_stdin_col(5), 5)

if __name__ == '__main__':
    unittest.main()