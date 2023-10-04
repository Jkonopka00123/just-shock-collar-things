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
from random import randint

# We only need the ImageGrab class from PIL
from PIL import ImageGrab

# TODO
#  API Call for shock, (pretty sure it works, just need to test it)
#  When hearhstone code works make it adapt to how much damage was taken, if i die, etc.
#  Reformat code to make it easier to read
#  Add ui to be able to adjust/reset parameters and variables and be able to pause program
#                   Would also allow for games to be swapped without restarting program
#  Add button to ui that will allow wearer to be shocked by the press of it
#  Stretch targets:
#                   Allow for new games to be added from ui including location and test of death indicator
#                   Make program into executable file
#                   Add db (or some form of storage) access and storage to save settings/death identifiers etc.




# API constants and variables
URL = "https://do.pishock.com/api/apioperate/"
USERNAME = "puppy73"
NAME = "TG_Bot_Script"
CODE = "17519CD8GAP"
API_KEY = "5c678926-d19e-4f86-42ad-21f5a76126db"
SHOCK = "0"
VIBRATE = "1"
BEEP = "2"
BEEP_INSTEAD_OF_SHOCK = 100  # 0-100, if 0 always shocks else chance of beep instead of shock


# intensity = "6"  # 1-100 strength of shock/vibration
# duration = "1"  # 1-15 length in seconds
# operator = "0"  # decides which action is taken


# 0 - shock
# 1 - vibrate
# 2 - beep // BEEP DOES NOT HAVE INTENSITY


# Hearthstone code just doesnt work, need more logic for hearthstone or perhaps api access to it
def hearthstone_damage_taken(starting_health, recognised_health):
    if starting_health > recognised_health:
        starting_health = recognised_health

    return starting_health


# Uses constants defined above and provided variables to send to api
# This will result in either a shock or beep
def call_shock(operator, duration, intensity):
    json_value = {"Username": USERNAME, "Name": NAME, "Code": CODE, "Intensity": intensity,
                  "Duration": duration, "Apikey": API_KEY, "Op": operator}
    r = requests.post(URL, json=json_value)
    return r


# setting variables used throughout program
shock_counter = 0
# Chosen game and number associated with it
#           0              1            2                   3
game = ["derptiny 2", "overwat 2", "warm stone", "warm stone but laptop"]
chosenGame = 0
print("game chosen", game[chosenGame])
# screen location for death marker
#                           D2                   Overwat                Warmstone           Warmstone Mobile
positionsForGrab = [[235, 79, 1000, 185], [3210, 45, 3400, 200], [1600, 990, 1860, 1300], [850, 800, 1070, 1030]]
#
sleep_times = [45, 15, 30, 30]

p1 = positionsForGrab[chosenGame][0]
p2 = positionsForGrab[chosenGame][1]
p3 = positionsForGrab[chosenGame][2]
p4 = positionsForGrab[chosenGame][3]

deathIdentifier = ["guardian down", "mrbreadlegs", None, None]
chosenDeath = deathIdentifier[chosenGame]
totalHealthArmour = 30


# Run forever unless you press Esc
while True:
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
    # and makes it reads more clean
    text = text.strip()

    if len(text) > 0:
        # hearthstone needs its own logic, and can't use the same as dest and overwat, it also still doesn't work
        # The plan is to have shock be dependent on damage taken, but again no work
        if chosenGame == 2 or chosenGame == 3:
            totalHealthArmour = hearthstone_damage_taken(totalHealthArmour,
                                                         sum(int(num) for num in re.findall(r'\d+', text)))
            print("new totalHealthArmour =", totalHealthArmour)

        # Shock amount will be determined by deaths, at the moment cannot be paused, or reset without stopping and
        # starting the program
        else:
            if chosenDeath in text.lower():
                print("YOU DIED LOL")

                # duration, intensity is dependent on num deaths stored in shock_counter
                shock_counter += 1
                intensity = shock_counter * 10
                if intensity > 100:
                    intensity = 100
                duration = shock_counter
                if duration > 15:
                    duration = 15

                # When condition is met, collar will vibrate as warning
                print(call_shock(VIBRATE, 2, intensity))

                print("DURATION:", duration)
                print("INTENSITY:", intensity)

                # for extra psychological fuckery, added chance to beep instead of shock
                if randint(1, 100) > BEEP_INSTEAD_OF_SHOCK:
                    print(call_shock(SHOCK, duration, intensity))
                else:
                    print(call_shock(BEEP, duration, intensity))

                print("SLEEPY TIME Zzz Zzz")
                time.sleep(1)
                # time.sleep(sleep_times[chosenGame])

        print("SHOCK COUNTER:", shock_counter)

        # after shock sleep to allow game state to be reset

    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()
