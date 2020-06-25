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
    IR = Infared.query.all()[-1]
    occupied = IR.value
    ts = IR.timestamp

    if occupied:
        msg = "TS: {} Temperature: {}   Humidity: {}   Solar Input: {}   Birdhouse is Occupied  ".format(ts, temperature, humidity, solar_input)
    else:
        msg = "Temperature: {}   Humidity: {}   Solar Input: {}   Birdhouse is Vacant".format(ts, temperature, humidity, solar_input)
    return msg

def DisplayScrollingLeft(txt, lcd):
    counter = 0
    for x in range(len(txt)):
        lcd.setCursor(0, 0)
        lcd.message(txt)
        lcd.setCursor(0, 1)
     # lcd.message(datetime.now().strftime('%b %d  %H:%M:%S'))
        sleep(.175)
        txt = txt[x+1:] + ' '
    return



PCF8574_address = 0x27
mcp = PCF8574_GPIO(PCF8574_address)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
mcp.output(3,1)     # turn on LCD backlight
lcd.begin(16,1)

while True:
    msg = getMessage()
    print(msg)
    DisplayScrollingLeft(msg, lcd)
    # print(msg)
