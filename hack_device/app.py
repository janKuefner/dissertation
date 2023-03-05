from picamera2 import Picamera2, Preview  # for taking pictures of the result
import easyocr  # https://github.com/JaidedAI/EasyOCR
from modules.robo_typer import Robo_typer
from time import sleep


class Hack_device(Robo_typer):
    def __init__(self):
        self.robo_typer = Robo_typer()
        self.is_password_cracked = False
        self.file_in_memory = open("wordlists/fasttrack.txt", "r")

    def bruteforce(self):
        self.robo_typer.initialize_I2Cs()  # initalize I2C
        for line in self.file_in_memory:
            print("I am typing:", line)
            self.robo_typer.type_string(line.strip('\n') + "   ")
            # picam2.capture_file("images/image01.jpg")  # picture size = 640 x 480
            # sleep(4)
            # result = reader.readtext('images/image01.jpg', detail=0)
            # print(result)


if __name__ == "__main__":
    hack_device = Hack_device()  # create a hack_device object
    hack_device.bruteforce()
    # picam2 = Picamera2()
    # picam2.start_preview(Preview.QTGL)
    # picam2.start()
    # reader = easyocr.Reader(['en'], gpu=False)  # load AI model into memory
    
    
