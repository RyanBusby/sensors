import RPi.GPIO as GPIO

class Infared():
    def __init__(self, ir_pin, led_pin):
        self.ir_pin = ir_pin
        self.led_pin = led_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ir_pin, GPIO.IN)
        GPIO.setup(led_pin, GPIO.OUT)

    def read(self):
        if GPIO.input(self.ir_pin) == GPIO.HIGH:
            GPIO.output(self.led_pin, GPIO.HIGH)
            return True

        else:
            GPIO.output(self.led_pin, GPIO.LOW)
            return False
