import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

troyka = 17
comp = 4
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]


GPIO.setmode(GPIO.BCM)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)



def decimal_to_binary(a, n):
    return [int (elem) for elem in bin(a) [2:].zfill(n)]

def to_leds(a):
    GPIO.output(leds, decimal_to_binary(a, 8))

def volume(n):
    mas=[0]*8
    for i in range(n):
        mas[7 - i] = 1
    return mas

def adc():
    k = 0 
    for i in range (7, -1, -1):
        k+=2**i
        GPIO.output(dac, decimal_to_binary(k, 8))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            k-=2**i
    return k

data = []
time_start = time.time()

voltage = 0

GPIO.output(troyka, 0)

print("Началась зарядка")
   
while voltage < 3.1:
    i = adc()
    if i!=0:
        voltage = 3.3*i/256
        print(i, '{:.2f}v'.format(voltage))
        GPIO.output(leds, volume(int(voltage/3.3*8)))
        data.append(voltage)

GPIO.output(troyka, 1)

print("Началась разрядка")

while voltage > 0.74:
    i = adc()
    if i!=0:
        voltage = 3.3*i/256
        print(i, '{:.2f}v'.format(voltage))
        GPIO.output(leds, volume(int(voltage/3.3*8)))
        data.append(voltage)

time_end = time.time()
time_experiment = time_end - time_start

with open('settings.txt', 'w') as outfile:
    outfile.write("Период измерений:  0.01" + '\n')
    outfile.write("время  измерения:")
    outfile.write(str(time_experiment) + '\n')
    outfile.write("Частота дискретизации:")
    outfile.write(str(3.3/256))

print("графики")

plt.plot(data)
plt.show()

GPIO.cleanup()