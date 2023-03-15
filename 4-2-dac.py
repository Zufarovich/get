import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary(a, n):
    return [int (elem) for elem in bin(a) [2:].zfill(n)]

t = int(input())
t = t/512
try:
    while True:
        for a in range(0, 255):
            GPIO.output(dac, decimal_to_binary(a, 8))
            sleep(t)

        for a in range(0, 255):
            GPIO.output(dac, decimal_to_binary(255 - a, 8))
            sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()