import pyautogui 
# For controlling mouse input
import keyboard
# For using keystroke to stop 

def autoClick():
    while True:
        pyautogui.click()
        if keyboard.is_pressed("."):
            # Uses . to break loop
            print("Break Loop")
            return


while True:
    if keyboard.is_pressed("`"):
        autoClick()
    if keyboard.is_pressed(","):
        print("Program Stop")
        break