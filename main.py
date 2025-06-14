import pytesseract
from PIL import Image

img = Image.open('number.png')

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open('phone_number.txt') as text_file:
    text_file.write(text)
