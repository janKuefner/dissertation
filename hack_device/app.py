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
        '''this method is the bruteforcing algorithm'''
        self.robo_typer.initialize_I2Cs()  # initalize I2C
        self.picam2.start_preview(Preview.QTGL)  # open a preview window
        self.picam2.start()  # start camera for further processing
        f = open("results.txt", "w")  # open results file in write mode
        f.write("")  # write nothing in the file / delete content
        f.close()  # close file
        for line in self.wrdlst:  # try every line entry in the wordlist
            print("\nI am typing:", line.strip('\n'))  # info for operator
            '''the following let`s the hack device type the line entry of the
            wordlist. In other words: The hacking device is typing one
            password'''
            self.robo_typer.type_string(line.strip('\n') + "   ")
            self.robo_typer.switch_module_outlet(3, 8)  # hit the enter key
            time.sleep(0.5)
            print("Taking photo")  # info for operator
            self.picam2.capture_file("images/image01.jpg")  # take picture
            print("transferring photo to text")  # info for operator
            '''the following AI converts the image to text'''
            result = self.reader.readtext('images/image01.jpg', detail=0)
            result_str = " ".join(result)  # merge the result list to a string
            print("This is what I read", result)  # info for operator
            f = open("results.txt", "a")  # open file for appending
            '''the following concenacts what was typed and the result text,
            which was AI converted from the camera'''
            new_line = line.strip('\n') + " - " + result_str + "\n"
            f.write(new_line)  # append the new line
            f.close()  # close file


if __name__ == "__main__":
    hack_device = Hack_device()  # create a hack_device object
    hack_device.bruteforce()  # start the bruteforce method
