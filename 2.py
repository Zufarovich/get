import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

p = GPIO.PWM(22, 1000)
q = GPIO.PWM(19, 1000)
p.start(0.0)
q.start(0.0)
print("Enter duty cycle")
dc = int(input())
p.ChangeDutyCycle(dc)
q.ChangeDutyCycle(dc)
input()
p.stop()
q.stop()
GPIO.cleanup()