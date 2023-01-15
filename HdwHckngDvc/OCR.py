import easyocr

print("yolo")
reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
result = reader.readtext('test.jpg')
print(result)
