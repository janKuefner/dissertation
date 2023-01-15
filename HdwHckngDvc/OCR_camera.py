from picamera2 import Picamera2, Preview
import easyocr
import time

picam2 = Picamera2()
# camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
# picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("images/test.jpg")
print("picture taken")
'''##################################'''
print("starting OCR...")
reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
result = reader.readtext('images/test.jpg')
print(result)
