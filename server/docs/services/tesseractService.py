import cv2
import pytesseract
from bidi.algorithm import get_display
from PIL import Image
import numpy as np
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def print_heb(text):
    print(get_display(text))

def get_cropped_img_str(imgUrl, x,y,w,h):
  
    img = cv2.imread(imgUrl)
    croppedImg =  img[y:y+h, x:x+w]
    

    # croppedImg = improve_img_readability(croppedImg)
    # test to check what img was cropped
    open_img(croppedImg)

    config='--oem 3 -c tessedit_char_whitelist=0123456789אבגדהוזחטיכלמנסעפצקרשת'
    image_str =  pytesseract.image_to_string(croppedImg, lang='heb')
    
    
    return image_str.replace("\n", "").replace("|", "")


def open_img(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)

def improved_tesseract():
    img = cv2.imread('wavy.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1,1), np.uint8)

    cv2.imwrite('thresh.png', img)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        
    for psm in range(6,13+1):
        config = '--oem 3 --psm %d' % psm
        txt = pytesseract.image_to_string(img, config = config, lang='eng')

# supposed to improve img readability
def improve_img_readability(img):
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    return cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

def search_text_in_string(str,text_before):
    str.split(text_before,1)[1]