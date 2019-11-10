import RPi.GPIO as GPIO
import os
from pyfiglet import Figlet
import sys
import time
from termcolor import colored, cprint


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


def light():
    print('    _------_')
    print('  -~        ~-')
    print(' -     _      -')
    print('-      |>      -')
    print('-      |<      -')
    print(' -     |>     -')
    print('  -    ||    -')
    print('   -   ||   -')
    print('    -__||__-')
    print('    |______|')
    print('    <______>')
    print('    <______>')
    print('       \/')


def _light():
    bulb = ['\n    _------_', '  -~        ~-', ' -     _      -', '-      |>      -', '-      |<      -',
            ' -     |>     -', '  -    ||    -', '   -   ||   -', '    -__||__-', '    |______|', '    <______>',
            '    <______>', '       \/']
    for i in bulb:
        print(i)


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


os.system('clear')
print('>> starting program...')
delay_print("<======================================================")


def display_text():
    os.system('clear')
    custom_fig = Figlet(font='graffiti')
    cprint(custom_fig.renderText('welcome to LSBU'), 'yellow')
    cprint("                    /********************************\\", 'yellow')
    cprint("                    *                                *", 'yellow')
    cprint("                    *      Use CTR + C to exit       *", 'red')
    cprint("                    *                                *", 'yellow')
    cprint("                    \********************************/\n", 'yellow')


display_text()
while True:
    GPIO.output(17, True)
    _light()
    time.sleep(2)
    GPIO.output(17, False)
    os.system('clear')
    display_text()
    time.sleep(1)




