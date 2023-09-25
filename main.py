# OCR Screen Scanner
# By Dornu Inene
# Libraries that you show have all installed
import cv2
import numpy as np
import pytesseract
import time
import re

# We only need the ImageGrab class from PIL
from PIL import ImageGrab

counter = 0
game = ["derptiny 2", "overwat 2", "warm stone"]
chosenGame = 0
print("game chosen", game[chosenGame])
#                           D2                   Overwat                Warmstone
positionsForGrab = [[235, 79, 1000, 185], [3210, 45, 3400, 200], [1600, 990, 1860, 1300]]

p1 = positionsForGrab[chosenGame][0]
p2 = positionsForGrab[chosenGame][1]
p3 = positionsForGrab[chosenGame][2]
p4 = positionsForGrab[chosenGame][3]
deathIdentifier = ["guardian down", "mrbreadlegs", "current"]
chosenDeath = deathIdentifier[chosenGame]
startingHealth = False
if chosenGame == 2:
    startingHealth = None
totalHealthArmour = 0

# Run forever unless you press Esc
while True:
    # This instance will generate an image from
    # the point of (115, 143) and (569, 283) in format of (x, y)

    while startingHealth == None:
        cap = ImageGrab.grab(bbox=(p1, p2, p3, p4))

        # For us to use cv2.imshow we need to convert the image into a numpy array
        cap_arr = np.array(cap)

        # This isn't really needed for getting the text from a window but
        # It will show the image that it is reading it from

        # cv2.imshow() shows a window display and it is using the image that we got
        # use array as input to image
        cv2.imshow("", cap_arr)

        # Read the image that was grabbed from ImageGrab.grab using    pytesseract.image_to_string
        # This is the main thing that will collect the text information from that specific area of the window
        text = pytesseract.image_to_string(cap)

        # This just removes spaces from the beginning and ends of text
        # and makes the the it reads more clean
        text = text.strip()
        if len(text) > 0:
            totalHealthArmour = sum(re.findall(r'\d+', text))
            startingHealth = 1

    cap = ImageGrab.grab(bbox=(p1, p2, p3, p4))

    # For us to use cv2.imshow we need to convert the image into a numpy array
    cap_arr = np.array(cap)

    # This isn't really needed for getting the text from a window but
    # It will show the image that it is reading it from

    # cv2.imshow() shows a window display and it is using the image that we got
    # use array as input to image
    cv2.imshow("", cap_arr)

    # Read the image that was grabbed from ImageGrab.grab using    pytesseract.image_to_string
    # This is the main thing that will collect the text information from that specific area of the window
    text = pytesseract.image_to_string(cap)

    # This just removes spaces from the beginning and ends of text
    # and makes the the it reads more clean
    text = text.strip()

    # If any text was translated from the image, print it

    # if len(text) > 0 and text.lower() == chosenDeath:
    if len(text) > 0 and chosenDeath in text.lower() or len(text) > 0 and totalHealthArmour < sum(re.findall(r'\d+', text)):
        # print(text)
        print("you died haha")
        print(counter)
        counter += 1
        # time.sleep(10)

    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()