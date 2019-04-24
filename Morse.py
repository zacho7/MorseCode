from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

led = LED(18)

#def close():
#    RPi.GPIO.cleanup()
#    win.destroy
    
def convert(message):
    morse = ""
    for letter in message:
        if letter != " ":
            morse += MORSE_CODE_DICT[letter] + " "
        else:
            morse = " "
            
    return morse

def blink(code):
    for letter in code:
        if letter == ".":
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(1)
        elif letter == "-":
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
            
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}      

win = Tk()
win.title("Morse code translator")

var = StringVar()

def translate():
    text = str(var.get())
    message = text.upper()
    morse_code = convert(message)
    print(morse_code)
    blink(morse_code)

textbox = Entry(win, textvariable = var)
textbox.grid(row = 0, column = 1)

translate = Button(text = "Translate", command = translate)
translate.grid(row = 1, column = 1)

#Exit = Button(text = "Close", command = close)
#Exit.grid(row = 2, column = 1) 

win.mainloop()