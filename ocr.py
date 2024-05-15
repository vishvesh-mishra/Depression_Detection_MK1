from PIL import Image 
from io import BytesIO
import requests
from pytesseract import pytesseract 


# Defining paths to tesseract.exe  
# and the image we would be using 
# path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
path_to_tesseract = r"D:/Softwares/Tesseract-OCR/tesseract.exe"

def get_text (Image_url) :
    # image_url = "https://scontent.cdninstagram.com/v/t51.29350-15/440914603_1148341009700329_8794870000605352566_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=18de74&_nc_ohc=5CeyvfsYTl0Q7kNvgFC79b1&_nc_ht=scontent.cdninstagram.com&edm=ANo9K5cEAAAA&oh=00_AfBYzJ7ICjFMv6Y-znZpjX0B7K-0l4etyKir0bocJWbYyA&oe=663BD352"

# Downloading the image from the URL
    response = requests.get(Image_url)
    img = Image.open(BytesIO(response.content))

    # Providing the tesseract  
    # executable location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)
    return text 
# Displaying the extracted text 
# print(text)