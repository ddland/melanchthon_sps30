import machine
import time
import struct
from melanchthon_sps30 import SPS
import os

basis_fn = 'melanchthon_%03d.csv' # filenaam in de form melanchthon_000.csv
delay = 5 # wacht 5 seconden na elke meting

# vind de eerste filenaam die nog niet bestaat
N = 0
running = True
while running:
    try:
        fn = basis_fn %(N) 
        vals = os.stat(fn)
        N+=1
    except OSError:
        running = False

# open een lege file
fh = open(fn, 'w')

# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)
sps = SPS(i2c)
sps.start_measurement()

# print beschrijving 
print(';'.join(str(ii) for ii in sps.data_header), file=fh)

# start metingen
measure = 1
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sps.get_data()
        # maak van de data een ; gescheiden string
        data = ';'.join(str(ii) for ii in sps.waarden)
        # print de data naar file (let op, er is maar weinig ruimte..
        print(data, file=fh)
        fh.flush()
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0
# sluit de file 
fh.close()
        
        
        
    