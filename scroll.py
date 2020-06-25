########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from dbsetup import db, Temp, Humid, Infared, SolarVolts
from time import sleep, strftime
from datetime import datetime


def getMessage():
    temperature = Temp.query.all()[-1].value
    humidity = Humid.query.all()[-1].value
    solar_input = SolarVolts.query.all()[-1].value
    vacancy = Infared.query.all()[-1].value
    if vacancy:
        msg = "Temperature: {}   Humidity: {}   Solar Input: {}   Birdhouse is Vacant".format(temperature, humidity, solar_input)
    else:
        msg = "Temperature: {}   Humidity: {}   Solar Input: {}   Birdhouse is Vacant".format(temperature, humidity, solar_input)
    return msg

def DisplayScrollingLeft(txt, lcd):
  txt = txt.strip() + ' '
  if len(txt) < 17:
    txt = txt + (16 * ' ' )
  while True:
     lcd.setCursor(0, 0)
     lcd.message(txt[:16])
     lcd.setCursor(0, 1)
     # lcd.message(datetime.now().strftime('%b %d  %H:%M:%S'))
     sleep(.175)
     txt = txt[1:] + txt[0]

PCF8574_address = 0x27
mcp = PCF8574_GPIO(PCF8574_address)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
mcp.output(3,1)     # turn on LCD backlight
lcd.begin(16,1)

while True:
    DisplayScrollingLeft(getMessage(), lcd)
