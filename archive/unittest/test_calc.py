import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(0, 1), 1)
        self.assertEqual(calc.add(-3, 3), 0)

    def test_switch_row_actuator(self):
        self.assertEqual(calc.switch_row_actuator(1, 1), "yolo")
        self.assertRaises(Exception, calc.switch_row_actuator, 0, 0)


if __name__ == '__main__':
    unittest.main()
