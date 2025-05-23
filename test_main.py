import unittest
import main

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(main.divide(8, 2), 4)


unittest.main()