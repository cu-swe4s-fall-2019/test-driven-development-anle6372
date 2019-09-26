import unittest
import data_viz



# Testing none input
class TestNone(unittest.TestCase):

    def test_boxplot_none(self):
        self.assertEqual(data_viz.boxplot(None, None), None)

    def test_histogram_none(self):
        self.assertEqual(data_viz.histogram(None, None), None)

    def test_combo_none(self):
        self.assertEqual(data_viz.histogram(None, None), None)

# Testing null input
class TestNull(unittest.TestCase):

    def test_boxplot_null(self):
        self.assertRaises(TypeError, lambda: data_viz.boxplot())

    def test_histogram_null(self):
        self.assertRaises(TypeError, lambda: data_viz.histogram())

    def test_combo_null(self):
        self.assertRaises(TypeError, lambda: data_viz.combo())

# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def test_boxplot_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(str('hi')))

    def test_histogram_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(str('hi')))

    def test_combo_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(str('hi')))


    def test_boxplot_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(4))

    def test_histogram_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(4))

    def test_combo_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(4))

    def test_boxplot_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(420.69))

    def test_histogram_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(420.69))

    def test_combo_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(420.69))

    def test_boxplot_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(True))

    def test_histogram_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(True))

    def test_combo_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(True))

if __name__ == '__main__':
    unittest.main()