import machine
import time
from melanchthon_sps30 import SPS

delay = 5 # wacht 5 seconden na elke meting

# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
# sensor verbonden met pin 0 en 1
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)
sps = SPS(i2c)

sps.start_measurement()

print(' '.join(str(ii) for ii in sps.data_header))
# start de metingen
measure = 1
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sps.get_data()
        data = ' '.join(str(ii) for ii in sps.waarden)
        print(data)
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0
        