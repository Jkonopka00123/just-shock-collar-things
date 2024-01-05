import tkinter as tk
import requests
import main


# URL = "https://do.pishock.com/api/apioperate/"
# USERNAME = "puppy73"
# NAME = "TG_Bot_Script"
# CODE = "17519CD8GAP"
# API_KEY = "5c678926-d19e-4f86-42ad-21f5a76126db"
SHOCK = "0"
VIBRATE = "1"
BEEP = "2"


def call_shock(operator, duration, intensity):
    # json_value = {"Username": USERNAME, "Name": NAME, "Code": CODE, "Intensity": intensity,
    #               "Duration": duration, "Apikey": API_KEY, "Op": operator}
    # r = requests.post(URL, json=json_value)
    # return r
    return "called call_shock"

def main_func():
    r = tk.Tk()
    r.title('Shock GUI')
    shock_button = tk.Button(r, text='Shock', width=25, command= lambda: print(main.call_shock(SHOCK, 1, 90)))
    beep_button = tk.Button(r, text='beep', width=25, command= lambda: print(call_shock(BEEP, 1, 90)))
    vibrate_button = tk.Button(r, text='vibrate', width=25, command= lambda: print(call_shock(VIBRATE, 1, 90)))
    main_button = tk.Button(r, text='launch', width=25, command= lambda: [r.destroy(), main.main_loop()])
    shock_button.pack()
    beep_button.pack(side="top")
    vibrate_button.pack()
    main_button.pack()
    r.mainloop()



# main_func()
if __name__ == "__main__":
    main_func()
