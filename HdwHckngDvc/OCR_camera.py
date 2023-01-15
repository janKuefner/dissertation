from picamera2 import Picamera2, Preview
import easyocr
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("images/image01.jpg")  # takes a picture with size 640 x 480 
print("picture taken")


print("starting OCR...")
reader = easyocr.Reader(['en'], gpu=False)  # load model into memory
result = reader.readtext('images/image01.jpg', detail=0)
print(result)
