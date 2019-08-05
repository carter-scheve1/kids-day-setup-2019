import RPi.GPIO as GPIO
import time
import sys
import socket
from getTemp import temp

# Configure GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Create mapping of segments to pin numbers
segments = [2, 17, 27, 22, 10, 9, 11]
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)

# Mapping of the 7 segments (plus the period)
'''
   -a-
|f     b|
   -g-
|e     c|
   -d-    .h   
'''
# 0 means on, 1 means off (opposite what you would think)
# [a, b, c, d, e, f, g, h]
# TODO fill in the correct values below
numbers = {
    '0':[0,0,0,0,0,0,1],
    '1':[1,0,0,1,1,1,1],
    '2':[0,0,1,0,0,1,0],
    '3':[?,?,?,?,?,?,?],
    '4':[?,?,?,?,?,?,?],
    '5':[?,?,?,?,?,?,?],
    '6':[?,?,?,?,?,?,?],
    '7':[?,?,?,?,?,?,?],
    '8':[?,?,?,?,?,?,?],
    '9':[?,?,?,?,?,?,?],
    '.':[?,?,?,?,?,?,?]
    }

# Code to light up and show a digit
def showCharacter(digit):
    for pin in range(0, 7):
        GPIO.output(segments[pin], numbers[digit][pin])

# TASK1 Display each digit (and decimal point) on 7-segment display
def TASK1():
    # TODO starter code below
    showCharacter('3')
    GPIO.cleanup()
    sys.exit(0)

# TASK2 Print the temperature on the console
def TASK2():
    # NOTE: To get the id here execute the command `ls /sys/bus/w1/devices`
    # TODO enter code below
    print("temperature")
    sys.exit(0)

# TASK3 Read the temperature and show the temp on the 7-segment display
def TASK3():
    # TODO enter code below
    sys.exit(0)


if __name__ == "__main__":
  try:
    #TASK1()
    TASK2()
    TASK3()    
  except:
    print("Ending program")
    GPIO.cleanup()
    sys.exit(1)
