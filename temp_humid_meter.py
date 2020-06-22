import RPi.GPIO as GPIO
import Freenove_DHT as DHT

class TempHumid():
    def __init__(self, pin):
        self.dht = DHT.DHT(pin)

    def read(self):
        chk = self.dht.readDHT11()
        if chk is self.dht.DHTLIB_OK:
            return self.dht.humidity, self.dht.temperature
        else:
            return
