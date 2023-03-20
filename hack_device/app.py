from picamera2 import Picamera2, Preview  # import library to use Pi`s webcam
import easyocr  # import AI image to text transformer
from modules.robo_typer import Robo_typer  # import the Robo_typer object
import time


class Hack_device(Robo_typer, Picamera2):
    def __init__(self):
        self.robo_typer = Robo_typer()  # create robo_Typer object
        self.picam2 = Picamera2()  # create camera object
        self.reader = easyocr.Reader(['en'], gpu=False)  # create easyocr objct
        self.wrdlst = open("wordlists/fasttrack.txt", "r")  # wordlist location

    def bruteforce(self):
        print("yolo")


if __name__ == "__main__":
    hack_device = Hack_device()  # create a hack_device object
    hack_device.bruteforce()  # start the bruteforce method
