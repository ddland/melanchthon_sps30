from sps30 import SPS30
import time 
# class voor de Sensirion SPS30
# Aansluiting (groene kant boven):
# ---------------
# |       12345 |
# | *  *   *  * |
# ---------------
# Pin layout:
# 1: VDD (5V)
# 2: SDA
# 3: SCL
# 4: GRND (for I2C)
# 5: GND

class SPS(SPS30):
    data_header = ['tijd s','pm 1.0 ug/m3','pm 2.5 ug/m3','pm 4.0 ug/m3','pm 10 ug/m3']
    waarden = [0,0,0,0,0]
    
    def get_data(self):
        self.read_data()
        self.waarden[0] = time.time()
        self.waarden[1:] = self.last_measurement[:4]