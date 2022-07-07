import cv2
import pytesseract


img = cv2.imread("wetransfer/IMG_0039.jpeg")

text = pytesseract.image_to_string(img)
print(text)
