import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(0, 1), 1)
        self.assertEqual(calc.add(-3, 3), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(0, 1), -1)
        self.assertEqual(calc.subtract(-3, 3), -6)


if __name__ == '__main__':
    unittest.main()
