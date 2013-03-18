import unittest
import sys

class TestFunctions1(unittest.TestCase):

    def setUp(self):
        # Import the project files
        self.f1 = __import__("functions-1")

    def test_tax_1(self):
        self.assertEqual(self.f1.tax(100, .5), 50)

    def test_tax_2(self):
        self.assertEqual(self.f1.tax(100, 0), 0)

    def test_tax_3(self):
        self.assertEqual(self.f1.tax(100, 2), 200)

    def test_tax_4(self):
        self.assertEqual(self.f1.tax(0, 2), 0)

    def test_mean_1(self):
        self.assertEqual(self.f1.mean([]), 0)

    def test_mean_2(self):
        self.assertEqual(self.f1.mean([1]), 1)

    def test_mean_3(self):
        self.assertEqual(self.f1.mean([1, 2, 4]), (1 + 2 + 4) / 3.0)

    def test_roots_1(self):
        self.assertEqual(self.f1.roots(1, 0, 0), (0, 0))

    def test_roots_2(self):
        self.assertEqual(self.f1.roots(1, 0, -1), (-1, 1))

    def test_roots_3(self):
        msg = "Don't worry if you can't get this one. The answer is (-1j, 1j)"
        self.assertEqual(self.f1.roots(1, 0, 1), (-1j, 1j), msg)



# Run the tests if this module was executed rather than imported
if __name__ == "__main__":
    unittest.main()
