import get_data
import unittest

# Testing none input
class TestNone(unittest.TestCase):

    def test_mean_none(self):
        self.assertEqual(get_data.read_stdin_col(None), None)


if __name__ == '__main__':
    unittest.main()