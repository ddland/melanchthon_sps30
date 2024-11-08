import machine
import time
import micropyGPS
import sys
import _thread
from melanchthon_sps30 import SPS
import os

basis_fn = 'melanchthon_%03d.csv'  # filenaam in de form melanchthon_000.csv
delay = 5  # wacht 5 seconden na elke meting


# GPS class voor het ophalen van data
class GPS:
    def __init__(self, uart, parser):
        self.uart = uart
        self.parser = parser
        self.running = False
        self.gpsdata = []

    def datetime(self, date, time):
        return '20%d%d%d:%d%d%f' % (date[2], date[1], date[0], time[0], time[1], time[2])

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            if self.uart.any():
                try:
                    data = self.uart.read().decode('utf-8')
                except UnicodeError:
                    continue  # skip invalid data
                except Exception as e:
                    print(e)
                    continue
                if data:
                    for ii in data:
                        self.parser.update(ii)
                if self.parser.valid:
                    self.gpsdata = [
                        self.datetime(self.parser.date, self.parser.timestamp),
                        self.parser.latitude,
                        self.parser.longitude,
                    ]
            else:
                time.sleep(0.01)


if __name__ == "__main__":
    # Initialiseer GPS en start thread
    uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))
    parser = micropyGPS.MicropyGPS(location_formatting='dd')
    gps = GPS(uart, parser)
    _thread.start_new_thread(gps.start, ())

    # Initialiseer SPS30-sensor
    i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
    sps = SPS(i2c)
    sps.start_measurement()

    # Zoek de eerste niet-bestaande bestandsnaam
    N = 0
    running = True
    while running:
        try:
            fn = basis_fn % (N)
            vals = os.stat(fn)
            N += 1
        except OSError:
            running = False

    # Open een nieuwe CSV-file en schrijf de headers
    fh = open(fn, 'w')
    headers = sps.data_header + ["gps_datetime", "latitude", "longitude"]
    print(';'.join(headers), file=fh)

    # Start metingen
    measure = True
    while measure:
        try:
            # Haal de SPS30-data op
            sps.get_data()
            sensor_data = ';'.join(str(ii) for ii in sps.waarden)
            
            # Haal de GPS-data op
            gps_data = gps.gpsdata if gps.gpsdata else ["N/A", "N/A", "N/A"]
            gps_data_str = ';'.join(str(ii) for ii in gps_data)

            # Combineer sensor- en GPS-data en sla op in bestand
            row_data = sensor_data + ";" + gps_data_str
            print(row_data, file=fh)
            fh.flush()
            time.sleep(delay)
        except KeyboardInterrupt:
            measure = False
            gps.stop()

    # Sluit het bestand af
    fh.close()
    print('All data has been recorded.')
