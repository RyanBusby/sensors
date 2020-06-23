import time
from datetime import datetime as dt

from infared_meter import IR
from temp_humid_meter import TempHumid
from solar_voltage_meter import SolarVoltage
from dbsetup import Temp, Humid, Infared, SolarVolts, db

ir = IR(13, 16)
th = TempHumid(40)
sv = SolarVoltage()

def insert_readings(irs, svs, hs, ts):
    [db.session.add(Infared(timestamp=l[0], value=l[1])) for l in irs]
    [db.session.add(SolarVolts(timestamp=l[0], value=l[1])) for l in svs]
    [db.session.add(Humid(timestamp=l[0], value=l[1])) for l in hs]
    [db.session.add(Temp(timestamp=l[0], value=l[1])) for l in ts]
    db.session.commit()

def run():
    irs = []
    svs = []
    hs = []
    ts = []
    counter = 0
    while True:
        counter += 1
        timestamp = dt.now()
        irs.append((timestamp, ir.read()))
        svs.append((timestamp, sv.read(0)))
        th_reading = th.read()
        if th_reading:
            hs.append((timestamp, th_reading[0]))
            ts.append((timestamp, th_reading[1]))
        time.sleep(1)
        if counter == 60:
            insert_readings(irs, svs, hs, ts)
            irs.clear()
            svs.clear()
            hs.clear()
            ts.clear()
            counter = 0

if __name__ == "__main__":
    run()



# check on sensors, init each gpio here, and drive measurements in loop that  controls db insertion

# run seperate file that sends "latest" data from db on the lcd and the touchscreen

# ultra sonic runs seperate process of waking and sleeping screensaver based on ultrasonic reading a nearby body
