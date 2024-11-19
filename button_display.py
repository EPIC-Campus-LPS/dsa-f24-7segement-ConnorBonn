import RPi.GPIO as GPIO
import tm1637
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.IN)

##Sets the clock and diod to pins
tm = tm1637.TM1637(clk=16, dio=21)
clear = [0,0,0,0]
tm.write(clear)
def stopwatch():
    GPIO.output(18,GPIO.HIGH)
    print("Timer Started")
    x = time.time()
    time.sleep(1)
    while True:
        if GPIO.input(23) == 0:
            GPIO.output(18,GPIO.LOW)
            x = time.time() - x
            print("Timer off")
            tm.number(int(x))
            time.sleep(3)
            GPIO.output(12,GPIO.LOW)
            break
            
while True:
    if GPIO.input(23) == 0:
        stopwatch()
        break
    else:
        continue