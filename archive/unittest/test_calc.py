import unittest
from calc import Yolo


class TestCalc(unittest.TestCase):

    def test_add(self):
        yolo_1 = Yolo()
        self.assertEqual(yolo_1.add(10, 1), 11)
        self.assertEqual(yolo_1.add(0, 1), 1)
        self.assertEqual(yolo_1.add(-3, 3), 0)


'''
    def test_switch_row_actuator(self):
        yolo = Yolo()
        self.assertEqual(yolo.switch_row_actuator(1, 1), "yolo")
        self.assertRaises(Exception, yolo.switch_row_actuator, 0, 0)
'''

if __name__ == '__main__':
    unittest.main()
