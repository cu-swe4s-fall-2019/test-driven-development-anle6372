import get_data
import unittest

# Testing none input
class TestNone(unittest.TestCase):

    def test_mean_none(self):
        self.assertEqual(get_data.read_stdin_col(None), None)

# Testing none input
class TestNull(unittest.TestCase):

    def test_mean_none(self):
        self.assertRaises(TypeError, lambda: get_data.read_stdin_col())

if __name__ == '__main__':
    unittest.main()