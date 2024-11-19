import RPi.GPIO as GPIO
import tm1637
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)

##Sets the clock and diod to pins
tm = tm1637.TM1637(clk=16, dio=21)
##Clears the dislay
clear = [0,0,0,0]
GPIO.output(12,GPIO.HIGH)
tm.write(clear)
time.sleep(1)
##Asks for user input
s = input("User: ")
##Scrolls the text accross the display
tm.scroll("Hello " + s, delay=250)
time.sleep(2)
##Turns off the power
GPIO.output(12,GPIO.LOW)