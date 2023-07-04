import pyautogui 
# For controlling mouse input
import keyboard
# For using keystroke to stop 

def autoClick():
    while True:
        pyautogui.click()
        if keyboard.is_pressed("."):
            # Uses . to break loop
            print("End")
            return


while True:
    if keyboard.is_pressed("`"):
        autoClick()