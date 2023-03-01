import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26]

number = [0, 0, 0, 0, 0, 0, 0, 0]

a = int(input())

for i in range(8):
    number[i] = int(a % 2)
    a = int(a / 2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)
time.sleep (10)
GPIO.output(dac, 0)

GPIO.cleanup()