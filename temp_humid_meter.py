import RPi.GPIO as GPIO
import Freenove_DHT as DHT

class TempHumid():
    def __init__(self, pin):
        dht = DHT.DHT(pin)

    def read():
        dht.readDHT11()
        if chk is dht.DHTLIB_OK:
            return dht.humidity, dht.temperature
        else:
            return
