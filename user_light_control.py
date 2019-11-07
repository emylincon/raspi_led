import RPi.GPIO as GPIO
import os
from pyfiglet import Figlet

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

os.system('clear')
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Welcome To LSBU'))
print("/*****************************************************\\")
print("*                                                     *")
print("*      Enter Off Or On to Control the Led Light       *")
print("*                                                     *")
print("\*****************************************************/\n")

while True:
    try:
        text = input(">> ").lower()
        if text == 'on':
            GPIO.output(17, True)
        elif text == 'off':
            GPIO.output(17, False)
        elif text == 'stop':
            break
        else:
            print("invalid input \n You Typed: ", text)
    except KeyboardInterrupt:
        print("\nProgramme Terminated\n")
        break
