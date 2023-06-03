import pytesseract as tes
tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

path = input("Enter the Image you want to know the data of:  ")
img = Image.open(path)

text = tes.image_to_string(img)

print(text)
