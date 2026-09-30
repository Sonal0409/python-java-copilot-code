import unittest

from myfile import multiply


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_mixed_sign_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)


if __name__ == "__main__":
    unittest.main()
