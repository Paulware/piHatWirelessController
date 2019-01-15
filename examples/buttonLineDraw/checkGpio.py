import RPi.GPIO as GPIO
import time

def checkKey (pin,msg):
   if GPIO.input(pin) == 0:
      print msg
      while GPIO.input(pin) == 0:
         time.sleep (0.01)

# pin numbers are interpreted as BCM pin numbers.13
GPIO.setmode(GPIO.BCM)
pinList = [(6,"Up"), (19, "Down"), (5,"Left"), (26,"Right"),
            (21,"Top"), (20,"Middle"), (16,"Downer"), (13, "Press")]
# Sets the pin as input and sets Pull-up mode for the pin.
for pin in pinList:
   GPIO.setup (pin[0],GPIO.IN, GPIO.PUD_UP)
   
while True:
    time.sleep(0.05)
    for pin in pinList: 
       checkKey (pin[0], "Pin " + str(pin[0]) + " " + pin[1])
       
# necessary?       
#!/usr/bin/python
# -*- coding:utf-8 -*-    