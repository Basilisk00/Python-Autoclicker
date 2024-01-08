import pyautogui # For controlling mouse input
import keyboard # For using keystroke to stop 
from tkinter import *

autoClicker_running = False #Global variable to track autoclicker status

def autoClick():
    global autoClicker_running # Global keyword needed to know that its not a local variable
    if keyboard.is_pressed('/'):
        autoClicker_running = False
        
    if autoClicker_running == True:
        pyautogui.click()
        root.after(1,autoClick) # Recursively calls itself every 1 ms
    else:
        print("Autoclicker stopped")
        swaptext()

def swaptext():
    global autoClicker_running
    if status.get() == 'Off':
        status.set('On')
        onOffButton.config(bg = "green") 
        autoClicker_running = True
    else:
        status.set('Off')
        onOffButton.config(bg="#FF0000")
        autoClicker_running = False
        
   
def buttonClick():
    swaptext()

def programRunning():
    global autoClicker_running
    if keyboard.is_pressed('.'):
        autoClick()   
    root.after(100,programRunning)
    
root = Tk()
root.title("Autoclicker")
root.resizable(width=False, height=False)
root.geometry("450x400+700+250")
status = StringVar(value = "Off") # Variable to show if clicker is running

#Label
autoClickerLabel = Label(root, text = "AUTOCLICKER", font = ("Tahoma",25) )
autoClickerLabel.pack(pady = 20)

#Status Button
onOffButton = Button(root, textvariable = status, font = ("Tahoma", 15), bg= "#FF0000", command= buttonClick) 
onOffButton.pack(pady = 30)

# Text 
armText = Label(root, text = "Press . to enable autoclicker loop", font = ("Tahoma", 15))
armText.pack()

endText = Label(root, text = "Press / to end autoclicker loop", font = ("Tahoma", 15))
endText.pack()

warningText = Label(root, text = "~ Warning: may need to press keyboard multiple times", font = ("Tahoma", 10))
warningText.pack()

root.after(0,programRunning) # Checks for user input
root.mainloop()