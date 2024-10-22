import network
import socket
from melanchthon_sps30 import SPS

## verbind de SPS30 met I2C
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)
sps = SPS(i2c)


## Configureer het accesspoint
# verbind en daarna kan je naar 192.168.4.1 om een meting uit te voeren
ssid = 'HHS-MELACHTHON'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

## start de SPS30 metingen (duurt 10 seconden)
sps.start_measurement()

## templates voor de website met en zonder data

webpage_start =  """
<!DOCTYPE HTML>
<html><head>SPS30 measurements</head>
<body><html>
<h2>measured values</h2>
<p>No data yet</p>
<form action="./measure">
<input type ="submit" value="measure" />
</form>
"""

webpage_data = """
<!DOCTYPE HTML>
<html><head>
<title>SPS30 measurements</title>
<style>
table, th, td {border: 1px solid black; border-collapse: collapse;}
th {text-align: left;}
</style>
</head>
<body>
<h2>measured values</h2>
<table >
 <tr >
       <th>tijd [s]</th>
      <th>PM1.0 mg/m^3</th>
      <th>PM2.5 mg/m^3</th>
      <th>PM4.0 mg/m^3</th>
      <th>PM 10 mg/m^3</th>
 </tr>
 <tr>
      <td> %d </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
 </tr>
</table>
<form action="./measure">
<input type ="submit" value="measure" />
</form>
</body>
</html>
"""

## start de hoofd-loop, waarin webserver en data uitgelezen worden

run = True
while run:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode('utf-8').lower()
        if request.find('get /measure?') >= 0:
            sps.get_data()
            html = webpage_data %tuple(sps.waarden)
        else:
            html = webpage_start
        conn.send(html)
        conn.close()
    except KeyboardInterrupt as e:
        run = False
s.close()
