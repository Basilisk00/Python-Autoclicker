import pyautogui 
# For controlling mouse input
import keyboard
# For using keystroke to stop 

while True:
    pyautogui.click()
    if keyboard.is_pressed("`"):
        # Uses ` to break loop
        print("End")
        break
