from Tkinter import *
import tkFont
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size=36, weight='bold')

def ledON():
    print("Button pressed")
    if GPIO.input(40):
        GPIO.output(40, GPIO.LOW)
        ledButton["text"] = "Unlock"
    else:
        GPIO.output(40, GPIO.HIGH)
        ledButton["text"] = "Lock"

def exitProgram():
    print("Exit button pressed")
    GPIO.cleanup()
    win.quit()

win.title("Unlock Gui")
win.geometry('800x480')

exitButton = Button(win, text="Exit", font=myFont, command=exitProgram, height=2, width=6)
exitButton.pack(side=BOTTOM)

ledButton = Button(win, text="Unlock", font=myFont, command=ledON, height=2, width=8)
ledButton.pack()

mainloop()
        
