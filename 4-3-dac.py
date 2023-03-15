import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0.0)
try:
    print("Enter duty cycle")
    dc = int(input())
    p.ChangeDutyCycle(dc)