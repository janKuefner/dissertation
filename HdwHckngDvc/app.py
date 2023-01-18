from time import sleep  # necessary for I2 communication
from picamera2 import Picamera2, Preview  # for taking pictures of the result
import easyocr  # https://github.com/JaidedAI/EasyOCR
from modules.robo_typer import Robo_typer


if __name__ == "__main__":
    robo_typer = Robo_typer()  # create a robo_typer object
    robo_typer.initialize_I2Cs()  # initalize I2C
    '''start up the camera'''
    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    sleep(2)  # give the camera some time to do the adjusting to environment
    ''' start up the easyocr model'''
    reader = easyocr.Reader(['en'], gpu=False)  # load AI model into memory
    '''loop the main program'''
    while (True):
        user_input = input("Enter String: ")
        robo_typer.hack_type_string(user_input)
        sleep(1)  # wait for the machine to type the character
        '''take a picture'''
        picam2.capture_file("images/image01.jpg")  # picture size = 640 x 480
        '''AI OCR the picture'''
        result = reader.readtext('images/image01.jpg', detail=0)
        print(result)
