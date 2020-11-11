import os
from time import sleep
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dir_path = os.path.dirname(__file__)
capture_path = os.path.join(dir_path, 'capture')

while True:
    if 'image.png' in (os.listdir(capture_path)):
        image_path = os.path.join(capture_path, 'image.png')
        img = Image.open(image_path).convert("L")
        text = pytesseract.image_to_string(img, lang='jpn')
        print(text.strip())
        img.close()
        os.remove(image_path)

    sleep(1)