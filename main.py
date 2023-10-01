# OCR Screen Scanner
# By Dornu Inene
# edited Jakub Konopka
# Libraries that you should have all installed
import cv2
import numpy as np
import pytesseract
import time
import re
import requests

# We only need the ImageGrab class from PIL
from PIL import ImageGrab

# TODO
#  API Call for shock,
#  when hearhstone code works make it adapt to how much damage was taken if i die, etc.



# TODO API TESTING STUFF
# duration = 2
# url = "https://do.pishock.com/api/apioperate/"
# temp = {"Username": "puppy73", "Name": "TG_Bot_Script", "Code": "17519CD8GAP", "Intensity": "6", "Duration": duration, "Apikey": "5c678926-d19e-4f86-42ad-21f5a76126db", "Op": "0"}
# r = requests.post(url, json=temp)
# print(r)


# Hearthstone code just doesnt work, need more logic for hearthstone or perhaps api access to it
def hearthstoneDamageTaken(startingHealth, recognisedHealth):
    if startingHealth > recognisedHealth:

        startingHealth = recognisedHealth
        
    return startingHealth


counter = 0
#           0              1            2                   3
game = ["derptiny 2", "overwat 2", "warm stone", "warm stone but laptop"]
chosenGame = 2
print("game chosen", game[chosenGame])
#                           D2                   Overwat                Warmstone           Warmstone Mobile
positionsForGrab = [[235, 79, 1000, 185], [3210, 45, 3400, 200], [1600, 990, 1860, 1300],[850, 800, 1070, 1030]]

p1 = positionsForGrab[chosenGame][0]
p2 = positionsForGrab[chosenGame][1]
p3 = positionsForGrab[chosenGame][2]
p4 = positionsForGrab[chosenGame][3]
deathIdentifier = ["guardian down", "mrbreadlegs", "current", "current"]
chosenDeath = deathIdentifier[chosenGame]
totalHealthArmour = 30

if chosenGame == 2 or chosenGame == 3:
    totalHealthArmour = 30

print("totalHealthArmour:",totalHealthArmour)

# Run forever unless you press Esc
while True:
    print("running main while")
    # This instance will generate an image from
    # the point of (115, 143) and (569, 283) in format of (x, y)

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
    # and (chosenDeath in text.lower() or len(text) > 0 and totalHealthArmour > sum(int(num) for num in re.findall(r'\d+', text))):
    if len(text) > 0:
        if chosenGame == 2 or chosenGame == 3:
            totalHealthArmour = hearthstoneDamageTaken(totalHealthArmour, sum(int(num) for num in re.findall(r'\d+', text)))
            print("new totalHealthArmour =", totalHealthArmour)
        else:
            print(text)
            print(counter)
            counter += 1
            # time.sleep(10)

    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()


