import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    text = input("Enter off or on: ").lower()
    if text == 'on':
        GPIO.output(17, True)
    elif text == 'off':
        GPIO.output(17, False)
    elif text == 'stop':
        break
    else:
        print("invalid input \n You Typed: ", text)
