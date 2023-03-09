import unittest
from robo_typer import Robo_typer


class TestCalc(unittest.TestCase):

    def test_add(self):
        robo_typer = Robo_typer()
        self.assertEqual(robo_typer.add(10, 1), 11)
        self.assertEqual(robo_typer.add(0, 1), 1)
        self.assertEqual(robo_typer.add(-3, 3), 0)

    def test_switch_row_actuator(self):
        robo_typer = Robo_typer()
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 0, 0)


if __name__ == '__main__':
    unittest.main()
