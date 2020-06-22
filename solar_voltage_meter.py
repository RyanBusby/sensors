import Adafruit_ADS1x15

class SolarVoltage():
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()

    def read(self):
        return self.adc.read_adc(0, gain=1)
