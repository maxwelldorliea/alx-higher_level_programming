import unittest

max_integer = __import__('6-max_integer').max_integer

class Max_IntegerTest(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([5, 9,19, 37]), 37)

    def test_max_float(self):
        self.assertEqual(max_integer([3.7, 56.79, 39.99, 10.55]), 56.79)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_negative(self):
        self.assertEqual(max_integer([-6, -9, -3, -2]), -2)

    def test_non_number(self):
        with self.assertRaises(TypeError):
                max_integer([3, 4, "alx", "holberton"])

if __name__ == '__main__':
    unittest.main()
