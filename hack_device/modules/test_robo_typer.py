import unittest
from robo_typer import Robo_typer


class TestRobo_typer(unittest.TestCase):

    def test_switch_row_actuator(self):
        robo_typer = Robo_typer()
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 0, 0)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 0, 1)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 0, 12)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, -1, 0)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, -1, -1)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, -1, 12)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 5, 0)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 5, -1)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 5, 12)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 8, 1)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 8, -1)
        self.assertRaises(Exception, robo_typer.switch_row_actuator, 8, 1)


if __name__ == '__main__':
    unittest.main()
