import LCD_1in44
import LCD_Config

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
import RPi.GPIO as GPIO
import time

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
   
def main():
   # pin numbers are interpreted as BCM pin numbers.13
   GPIO.setmode(GPIO.BCM)
   pinList = [(6,"Up"), (19, "Down"), (5,"Left"), (26,"Right"),
               (21,"Top"), (20,"Middle"), (16,"Downer"), (13, "Press")]
   # Sets the pin as input and sets Pull-up mode for the pin.
   for pin in pinList:
      GPIO.setup (pin[0],GPIO.IN, GPIO.PUD_UP)
     
   LCD = LCD_1in44.LCD()
   
   print "**********Init LCD**********"
   Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
   LCD.LCD_Init(Lcd_ScanDir)
   
   image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
   draw = ImageDraw.Draw(image)
   #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
   print "***draw line"
   draw.line([(0,0),(127,0)], fill = "BLUE",width = 5)
   draw.line([(127,0),(127,127)], fill = "BLUE",width = 5)
   draw.line([(127,127),(0,127)], fill = "BLUE",width = 5)
   draw.line([(0,127),(0,0)], fill = "BLUE",width = 5)
   print "***draw rectangle"
   draw.rectangle([(18,10),(110,20)],fill = "RED")
   
   print "***draw text"
   draw.text((33, 22), 'WaveShare ', fill = "BLUE")
   draw.text((32, 36), 'Electronic ', fill = "BLUE")
   draw.text((28, 48), '1.44inch LCD ', fill = "BLUE")

   LCD.LCD_ShowImage(image,0,0)
   LCD_Config.Driver_Delay_ms(500)
   
   #image = Image.open('time.bmp')
   #LCD.LCD_ShowImage(image,0,0)
   
   while True:
      time.sleep(0.05)
      if GPIO.input(21) == 0: # Top
         image = Image.open('time.bmp')
         LCD.LCD_ShowImage(image,0,0)
      elif GPIO.input(20) == 0: # Middle
         image = Image.open('sky.bmp')
         LCD.LCD_ShowImage(image,0,0)
      elif GPIO.input(16) == 0: # bottom button
         image = Image.open('rick.bmp')
         LCD.LCD_ShowImage(image,0,0)
      elif GPIO.input(5) == 0: # left
         image = Image.open('radiation.bmp')
         LCD.LCD_ShowImage(image,0,0)
      elif GPIO.input(26) == 0: # right button
         image = Image.open('vader.bmp')
         LCD.LCD_ShowImage(image,0,0)
      elif GPIO.input(6) == 0: # up button
         image = Image.open('yellowGhost.bmp')
         LCD.LCD_ShowImage(image,0,0)  
      elif GPIO.input(19) == 0: # down button
         image = Image.open('battleBlock.bmp')
         LCD.LCD_ShowImage(image,0,0)         
      elif GPIO.input(13) == 0: # press joystick
         image = Image.open('flower.bmp')
         LCD.LCD_ShowImage(image,0,0)
      else: 
         for pin in pinList: 
            checkKey (pin[0], "Pin " + str(pin[0]) + " " + pin[1], LCD)
	
if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()