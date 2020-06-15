from time import sleep,strftime
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from datetime import datetime

try:
    lcd_rs = 26
    lcd_en = 19
    lcd_d4 = 13
    lcd_d5 = 6
    lcd_d6 = 5
    lcd_d7 = 11
    lcd_backlight = 4
    lcd_columns = 16
    lcd_rows = 2
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    while True:
        lcd.home()
        lcd.set_cursor(0, 1)
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S'))

        lcd.home()
        lcd.set_cursor(0, 0)
        messages='Text is moving left'
        lcd.message(messages)
        for i in range(0,4):
            sleep(0.5)
            lcd.move_left()
except:
    pass
    GPIO.cleanup()

finally:
    GPIO.cleanup()
