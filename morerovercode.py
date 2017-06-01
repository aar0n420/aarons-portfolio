GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
sleep(1)
GPIO.output(23, GPIO.LOW)

GPIO.cleanup()




import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def forward(x):
    GPIO.output(10, GPIO.HIGH)
    sleep(1)
    GPIO.output(10, GPIO.LOW)

def backward(x):
    GPIO.output(13, GPIO.HIGH)
    sleep(1)
    GPIO.output(15, GPIO.LOW)

forward(4)
sleep(0.75)
reverse(4)

GPIO.cleanup()
