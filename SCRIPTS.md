## Code
De bestanden (sps_xxx.py) maken op verschillende manieren gebruik van de sensor en geven de data weer. Van opslaan tot via de telefoon uitlezen, er zijn veel mogelijkheden. 
Wil je de sensor zonder computer (Thonny) gebruiken, dan moet de sps_xxx.py file hernoemd worden naar main.py (en alle afhankelijkheden moeten op de Raspberry Pi Pico in de lib folder staan), deze file wordt automatisch uitgevoerd als de Rasbperry Pi Pico van stroom voorzien wordt. Om data daarna van de Raspberry Pi Pico af te lezen moet die weer aangesloten worden op de computer om de bestanden van de microcontroller naar de computer te kopieren. 

### SPS Aansluiten
De Sensirion SPS-30 sensor heeft 5V voeding nodig. Daarnaast moeten de I2C verbindingen juist aangelosten zijn en moeten 2 verbindingen met de GND (ground, aarde) pinnen van de Raspberry Pi Pico aangesloten worden om de sensor op de juiste manier uit te kunnen lezen. 
In onderstaand figuur staan de verbindingen getekend om de SPS-30 aan te sluiten op I2C pinnen 0 en 1.
[aansluiting SPS-30](afbeeldingen/SPS30_Pico_bb.jpg).

#### SPS print - weergeven van data op via het scherm
Het bestand `sps_print.py` geeft de gemeten waarden weer op het scherm via Thonny of de serial port. Door de serial port de data weg te laten schrijven naar een bestand kan, met de Raspberrypi Pico altijd aangesloten aan een laptop, data naar een file geschreven worden.  

#### SPS save - sla data lokaal op
Het bestand `sps_save.py` slaat de data gemeten door de sensor op. Opslag van de Raspberry Pi Pico is beperkt (er blijft ongeveer 1.5 Mb over na uploaden van de code) en moet dus regelmatig van de sensor gedownload worden. 

### SPS display - geef data weer op een display
De SPS-30 is op dezelde manier aangesloten als bij de vorige mogelijkheden, maar er is een extra OLED scherm toegevoegd:

[aansluiting SPS-30 met scherm](afbeeldingen/SPS30_display_bb.jpg)

Aansluiting van de SPS-30 is op I2C bus 0, terwijl het scherm op I2C bus 1 is aangesloten, elk met eigen instellingen voor de I2C bus. 

Uitvoeren van het bestand `sps_display.py` geeft de gemeten waarden weer op een OLED scherm met de SSD1306 driver. Door de file te hernomeen naar `main.py` kan je zo in het veld de meetwaarden aflezen. Ook zou je dit script kunnen combineren met `sps_save.py` en zo niet alleen de waarden direct zien, maar ook kunnen opslaan.

### GPS
Als je fijnstof buiten wilt gaan meten is het handig om een GPS-sensor toe te voegen aan het systeem. Je kan dan vanuit de GPS data de locatie, maar ook de tijd bijhouden en zo de fijnstofconcentraties op verschillende plekken met elkaar vergelijken. 

Afhankelijk of je een breadboard gebruikt of de sensoren direct op de Raspberry Pi Pico aansluit kan ze op de volgende manieren aansluiten:
[aansluiten SPS-30 met GPS en breadboard](afbeeldingen/SPS30_gps_bb.jpg)
[aansluiten SPS-30 met GPS](afbeeldingen/SPS30_gps_v2_bb.jpg)

De GPS sensor is via een UART (serial) verbinding aangesloten en geeft zijn data door aan de Raspberry Pi Pico. Deze code is wat complexer omdat op de 2e core van de Raspberry Pi Pico de GPS sensor continu uitgelezen wordt. Onafhankelijk vna de fijnstof metingen wordt de locatie en de tijd gemeten. 

Uitvoeren van het bestand `sps_gps.py` geeft de locatie en tijd naast de gemeten fijnstof concentratie weer op het scherm via Thonny of de serial port.

Om ook de data weg te schrijven naar file kan het bestand `sps_gps_save.py` gebruikt worden. Locatie en tijd worden nu ook weggeschreven.

### Raspberry Pi Pico als webserver

Door het script `sps_webserver.py` uit te voeren start de Raspberry Pi Pico een access-point (`HHS-MELACHTHON`) waar je op kan inloggen met je computer of telefoon (password: 123456789). Daarna kan je naar de website: [192.168.4.1](http://192.168.4.1) gaan waar je de metingen kan uitvoeren (en aflezen). Data kan je kopieren van de website naar een logbestand, of je kan via andere tools (bijvoorbeeld een python scripts) automatisch elke paar seconden de data uitlezen.  
