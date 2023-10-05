import cv2
import numpy as np
import pytesseract
import time
import re
import requests
from random import randint
from PIL import ImageGrab
import guiTests

# TODO
#  When hearhstone code works make it adapt to how much damage was taken, if i die, etc.
#  Reformat code to make it easier to read (KINDA DONE BY chatGPT)
#  Add ui to be able to adjust/reset parameters and variables and be able to pause program
#                   Would also allow for games to be swapped without restarting program
#  Add button to ui that will allow wearer to be shocked by the press of it
#  Stretch targets:
#                   Allow for new games to be added from ui including location and test of death indicator
#                   Make program into executable file
#                   Add db (or some form of storage) access and storage to save settings/death identifiers etc.

# Constants
URL = "https://do.pishock.com/api/apioperate/"
USERNAME = "puppy73"
NAME = "just-shock-collar-things"
CODE = "17519CD8GAP"
API_KEY = "5c678926-d19e-4f86-42ad-21f5a76126db"
SHOCK = "0"
VIBRATE = "1"
BEEP = "2"
BEEP_INSTEAD_OF_SHOCK = 0  # 0-100, if 0 always shocks else chance of beep instead of shock


# Game-specific settings
game_names = ["derptiny 2", "overwat 2", "warm stone", "warm stone but laptop"]
chosen_game = 0  # Default chosen game index
print("Game chosen:", game_names[chosen_game])

positions_for_grab = [
    [235, 79, 1000, 185],   # D2
    [3210, 45, 3400, 200],  # Overwat
    [1600, 990, 1860, 1300],  # Warmstone
    [850, 800, 1070, 1030]  # Warmstone Mobile
]

sleep_times = [45, 15, 30, 30]

x1, y1, x2, y2 = positions_for_grab[chosen_game]

death_identifiers = ["guardian down", "mrbreadlegs", None, None]
chosen_death = death_identifiers[chosen_game]
total_health_armor = 30



# Helper functions
def hearthstone_damage_taken(starting_health, recognised_health):
    if starting_health > recognised_health:
        starting_health = recognised_health
    return starting_health

def call_shock(operator, duration, intensity):
    # json_value = {"Username": USERNAME, "Name": NAME, "Code": CODE, "Intensity": intensity,
    #               "Duration": duration, "Apikey": API_KEY, "Op": operator}
    # r = requests.post(URL, json=json_value)
    # return r
    return "called call_shock"

def capture_window(x1, x2, y1, y2):
    cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    cap_arr = np.array(cap)
    cv2.imshow("", cap_arr)
    text = pytesseract.image_to_string(cap).strip()
    return text


# print(call_shock(VIBRATE,1,1))

shock_counter = 0

# Main loop
def main_loop():
    global shock_counter
    while True:
        text = capture_window(x1, x2, y1, y2)

        if len(text) > 0:
            if chosen_game == 2 or chosen_game == 3:
                total_health_armor = hearthstone_damage_taken(total_health_armor, sum(int(num) for num in re.findall(r'\d+', text)))
                print("New totalHealthArmor =", total_health_armor)
            else:
                if chosen_death in text.lower():
                    print("YOU DIED LOL")
                    shock_counter += 1
                    intensity = shock_counter * 10
                    intensity = min(100, intensity)
                    duration = min(shock_counter, 15)

                    print("DURATION:", duration)
                    print("INTENSITY:", intensity)

                    if randint(1, 100) > BEEP_INSTEAD_OF_SHOCK:
                        print(call_shock(SHOCK, duration, intensity))
                    else:
                        print(call_shock(BEEP, 1, 1))

                    print("SLEEPY TIME Zzz Zzz")
                    time.sleep(1)

            print("SHOCK COUNTER:", shock_counter)

        if cv2.waitKey(1) == 27:  # Break the loop when Esc is pressed
            cv2.destroyAllWindows()
            # guiTests.main_func()
            break

if __name__ == "__main__":
    main_loop()
  

# Close all OpenCV windows
