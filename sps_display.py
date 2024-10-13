import machine
import time
import struct
from melanchthon_sps30 import SPS
import os
import ssd1306

def write(display, text, x,y):
    """ send the text at (x,y) coordinates to the display.
    If more then one line, send a list of lines to the display
    x (0 - 62), y (16 - 64)
    """ 
    display.fill(0) # black
    if isinstance(text, list):
        for ii in range(len(text)):
            display.text(text[ii], x[ii], y[ii])
    else:
        display.text(text,x,y)
    display.show()

delay = 5 # wacht 5 seconden na elke meting

# maak verbinding met het scherm
i2c1 = machine.I2C(1, sda = machine.Pin(14), scl = machine.Pin(15))
display = ssd1306.SSD1306_I2C(64,64, i2c1)

write(display, 'starting', 0,16)
# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
i2c0 = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)
sps = SPS(i2c0)
sps.start_measurement()


# start metingen
measure = 1
t0 = time.time()
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sps.get_data()
        # maak van de data een ; gescheiden string
        data = sps.waarden
        write(display, ['t:%d' %(data[0] - t0), '1.0:%2.2f' %(data[1]), '2.5:%2.2f' %(data[2])], [0,0,0], [16,32,48])
        # print de data naar file (let op, er is maar weinig ruimte..
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0        
        
        
    