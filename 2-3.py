import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while (1):
    for i in range(8):
        number[i] = GPIO.input(aux[i])
    GPIO.output(leds, number)