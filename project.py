import openai
import pytesseract as tes
tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

path = input("Enter the Image you want to know the data of:  ")
img = Image.open(path)

text = tes.image_to_string(img)
# print(text)
openai.api_key = "OPEN AI KEY"

messages = []

system_msg = """First input is given then List down the dishes in a table of human readable  column and row wise configuration . only provide the list of given items and do not mention calories .
Then follow with the following prompt 
you are assisting user in deciding foods and dishes that the user is interested in.
You also provide them with the nutritional values of the food 
Only give relevant 5 dishes to user when asked for a particular disk"""


messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready!")
messages.append({"role": "user", "content": text})

while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
