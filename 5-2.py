import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4
troyka = 17
levels = len(dac)
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)    
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

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

def adc2():
    k=0
    for value in range(8):
        k+=2**value
        dacc = decimal_to_binary(value, 8)
        GPIO.output(dac, dacc)
        sleep(0.0005)
        compValue = GPIO.input(comp)
        if compValue == 0:
            k-=2**value
    return k

def adc3():
    k = 128
    step = 128
    for i in range(8):
        dacc = decimal_to_binary(k, 8)
        GPIO.output(dac, dacc)
        sleep(0.005)
        compValue = GPIO.input(comp)
        step =  int(step/2)
        if compValue == 0:
            k -=step
        else:
            k+=step
    return k

def volume(n):
    mas=[0]*8
    for i in range(n):
        mas[7 - i] = 1
    return mas

GPIO.cleanup()