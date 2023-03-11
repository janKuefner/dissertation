from unittest.mock import Mock
from robo_typer import Robo_typer


Robo_typer = Mock()
Robo_typer.yolo(1, 2)
Robo_typer.yolo(1, 2)
print(Robo_typer.yolo.assert_called_once())
