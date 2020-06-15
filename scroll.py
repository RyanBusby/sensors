########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime

def DisplayScrollingLeft(txt, lcd):
  txt = txt.strip() + ' '
  if len(txt) < 17:
    txt = txt + (16 * ' ' )
  while True:
     lcd.set_cursor(0, 0)
     lcd.message(txt[:16])
     lcd.set_cursor(0, 1)
     lcd.message(datetime.now().strftime('%b %d  %H:%M:%S'))
     time.sleep(0.5)
     txt = txt[1:] + txt[0]

PCF8574_address = 0x27
mcp = PCF8574_GPIO(PCF8574_address)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

DisplayScrollingLeft('This scrolls to the left.', lcd)
