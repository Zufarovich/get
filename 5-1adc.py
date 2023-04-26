import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17
levels = len(dac)
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)    
GPIO.setup(comp, GPIO.IN)

def decimal_to_binary(a, n):
    return [int (elem) for elem in bin(a) [2:].zfill(n)]

def adc():
    for value in range(256):
        dacc = decimal_to_binary(value, 8)
        GPIO.output(dac, dacc)
        compValue = GPIO.input(comp)
        sleep(0.005)
        if compValue==0:
            return value

while True:
    i = adc()
    if i!=0:
        print(i, '{:.2f}v'.format(3.3*i/256))

