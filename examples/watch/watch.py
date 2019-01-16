import LCD_1in44
import LCD_Config
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
import RPi.GPIO as GPIO
import time
import os

def checkKey (pin,msg, LCD):
   if GPIO.input(pin) == 0:
      showText (msg,LCD)
      print msg
      while GPIO.input(pin) == 0:         
         time.sleep (0.01)
 
def showText (msg,LCD):
   image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
   draw = ImageDraw.Draw(image)
   print "***draw text"
   draw.text((33, 22), msg, fill = "BLUE")
        

# This function retrieves the x, y coordinates based on a "tick" mark, which ranges between 0 and 60
# A "tick" of 0 is at the top of the circle, 30 is at the bottom, 45 is at the "9 o'clock" position, etc.
# The "stretch" is how far from the origin the x, y return values will be
# "originx" and "originy" will be where the center of the circle is (almost always the center of the window)
def getTickPosition(tick, stretch=1, originx=64, originy=64):
   
    # The cos() and sin()
    tick -= 15 # change 0 degree from 3oclock to 12oclock

    # ensure that tick is between 0 and 60
    tick = tick % 60

    tick = 60 - tick

    # the argument to sin() or cos() needs to range between 0 and 2 * math.pi
    # Since tick is always between 0 and 60, (tick / 60.0) will always be between 0.0 and 1.0
    # The (tick / 60.0) lets us break up the range between 0 and 2 * math.pi into 60 increments.
    x =      math.cos(2 * math.pi * (tick / 60.0))
    y = -1 * math.sin(2 * math.pi * (tick / 60.0)) # "-1 *" because in Pygame, the y coordinates increase going down (the opposite of how they normally go in mathematics)

    # sin() and cos() return a number between -1.0 and 1.0, so multiply to stretch it out.
    x *= stretch
    y *= stretch

    # Then do the translation (i.e. sliding) of the x and y points.
    # NOTE: Always do the translation addition AFTER doing the stretch.
    x += originx
    y += originy

    return x, y


def drawHands(imageDraw, hour,minute,seconds):
   print "drawHands(" + str(hour) + "," + str(minute) + "," + str(seconds) + ")" 
   x,y = getTickPosition (hour*5,32)
   imageDraw.line((64,64,x,y),fill="BLUE",width=5)  
   
   x,y = getTickPosition (minute,64)
   imageDraw.line((64,64,x,y),fill="BLUE",width=3)                  

   x,y = getTickPosition (seconds,64)
   imageDraw.line((64,64,x,y),fill="RED",width=1)                  

   
def main():
   # get the current time

   # pin numbers are interpreted as BCM pin numbers.13
   GPIO.setmode(GPIO.BCM)
   pinList = [(6,"Up"), (19, "Down"), (5,"Left"), (26,"Right"),
              (21,"Top"), (20,"Middle"), (16,"Bottom"), (13, "Press")]
              
   months = ["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
              
   # Sets the pin as input and sets Pull-up mode for the pin.
   for pin in pinList:
      GPIO.setup (pin[0],GPIO.IN, GPIO.PUD_UP)
     
   LCD = LCD_1in44.LCD()
   
   print "**********Init LCD**********"
   Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
   LCD.LCD_Init(Lcd_ScanDir)
   LCD_Config.Driver_Delay_ms(500)
   time.sleep (0.5)

   
   while (True):
      image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
      draw = ImageDraw.Draw(image)         
      draw.arc ((0,0,127,127), 0, 360, fill="WHITE") 
      now = time.localtime()
      # print str(time.localtime())
      hour = now[3] % 12 # now[3] ranges from 0 to 23, so we mod 12.
      minute = now[4]
      second = now[5] + (time.time() % 1) # add the fraction of a second we get from time.time() to make a smooth-moving seconds hand
      drawHands (draw,int(hour),int(minute),int(second))
      LCD.LCD_ShowImage(image,0,0); 
      startTime = time.time() 
      while ( time.time() - startTime < 1): 
         if GPIO.input(21) == 0: # Top
            msg = "date -s \"" + str(now [2]) + " " + months[int(now[1])] + " " + str(now[0]) + " " + \
                  str((now[3]+1)%24 ) + ":" + str(minute) + ":" + str(int(second)) + "\""
            print msg
            os.system (msg)
            break;
         elif GPIO.input(20) == 0: # Middle
            msg = "date -s \"" + str(now [2]) + " " + months[int(now[1])] + " " + str(now[0]) + " " + \
                  str(now[3] ) + ":" + str((minute+1)%60) + ":" + str(int(second)) + "\""
            print msg
            os.system (msg)
            break;
         elif GPIO.input(16) == 0: # Bottom
            msg = "date -s \"" + str(now [2]) + " " + months[int(now[1])] + " " + str(now[0]) + " " + \
                  str(now[3] ) + ":" + str(minute) + ":" + str((int(second)+1)%60) + "\""
            print msg
            os.system (msg)
            break;
         
         
         time.sleep (0.1)

   
print "date -s DD MMM YYYY HH:MM:SS"
main()