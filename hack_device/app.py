from picamera2 import Picamera2, Preview  # for taking pictures of the result
import easyocr  # https://github.com/JaidedAI/EasyOCR
from modules.robo_typer import Robo_typer
from time import sleep

# implement Hack_device object,
# methods bruteforce(dictionary, sleep), injection(db_type)


if __name__ == "__main__":
    robo_typer = Robo_typer()  # create a robo_typer object
    robo_typer.initialize_I2Cs()  # initalize I2C
    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    reader = easyocr.Reader(['en'], gpu=False)  # load AI model into memory
    file_in_memory = open("wordlists/fasttrack.txt", "r")
    for line in file_in_memory:
        print("I am typing:", line)
        robo_typer.type_string(line.strip('\n') + "   ")
        picam2.capture_file("images/image01.jpg")  # picture size = 640 x 480
        sleep(4)
        result = reader.readtext('images/image01.jpg', detail=0)
        print(result)
