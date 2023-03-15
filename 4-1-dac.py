import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary(a, n):
    return [int (elem) for elem in bin(a) [2:].zfill(n)]

try:
    while True:
        print("Enter number from 0 to 255")
        a = input()
        if a == 'q' or not a.isdigit() or int(a) < 0 or int(a) > 255 or isfloat(a):
            break
        a = int(a)
        u = 3.2*(a/255)
        print("Voltage ")
        print(u)
        GPIO.output(dac, decimal_to_binary(a, 8))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()