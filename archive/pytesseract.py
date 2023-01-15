'''working file of pytesseract'''
import pytesseract
import cv2
img = cv2.imread('images/test0001.jpg')  # image must be small, tho
print(pytesseract.image_to_string(img))
