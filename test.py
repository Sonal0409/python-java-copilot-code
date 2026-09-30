import unittest

from app import add


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-4, -6), -10)

    def test_mixed_sign_numbers(self):
        self.assertEqual(add(-3, 8), 5)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 9), 9)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_large_numbers(self):
        self.assertEqual(add(10**18, 10**18), 2 * 10**18)


if __name__ == "__main__":
    unittest.main()
