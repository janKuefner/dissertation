from picamera2 import Picamera2, Preview
import easyocr
import time

picam2 = Picamera2()
# camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
# picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
for x in range(6):
    print(x)
    time.sleep(2)
    picam2.capture_file("images/test{0:04d}.jpg".format(x))
    print("picture taken")


print("starting OCR...")
reader = easyocr.Reader(['en'], gpu=False)  # this needs to run only once to load the model into memory
print("Los geht es")
print("Yolo.jpg wird angeschaut")
result = reader.readtext('images/test0000.jpg', detail = 0)
print(result)
print("")
print("")
print("test0001.jpg")
print("")
result = reader.readtext('images/test0001.jpg', detail = 0)
print(result)
print("")
print("")
print("test0002.jpg")
print("")
result = reader.readtext('images/test0002.jpg', detail = 0)
print(result)
