# Melanchthon en Fijnstof
Het meten van fijnstof kan inzichtelijk maken hoe schoon de lucht in je omgeving is. Er zijn wereldwijd richtlijnen voor de maximale fijnstof concentratie waar je aan blootgesteld zou mogen worden. Voor fijnstof heeft de [WHO](https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health) de volgende AQG levels (air-quality-guidelines) voorgeschreven:

------------------------------
|PM | gemiddelde over | AQG  |
------------------------------
|PM2.5 | jaarlijks | 5$\mu$g/m$^3$  |
|PM2.5 | 24 uur    | 15$\mu$g/m$^3$ |
|PM10  | jaarlijks | 15$\mu$g/m$^3$  |
|PM10  | 24 uur    | 45$\mu$g/m$^3$ |
------------------------------

In [Nederland](https://www.infomil.nl/onderwerpen/landbouw/stof/handreiking-fijn-1/juridisch-kader/wettelijke-eisen/) zijn andere waarden als grenswaarden ingesteld:

------------------------------
|PM | gemiddelde over | AQG  |
------------------------------
|PM2.5 | jaarlijks | 25$\mu$g/m$^3$  |
|PM10  | jaarlijks | 40$\mu$g/m$^3$  |
|PM10  | 24 uur    | 50$\mu$g/m$^3$ |
------------------------------

In dit project ga je onderzoeken welke blootstelling je in je eigen omgeving ervaart. En hoe nauwkeurig deze blootstelling is te meten. Het lectoraat [Smart Sensor Systems van de Haagse Hogeschool](https://www.dehaagsehogeschool.nl/onderzoek/lectoraten/smart-sensor-systems) doet zelf ook actief onderzoek naar blootstelling aan verschillende grootheden, waar fijnstof er een van is.

## Onderzoeksvragen
Om je onderzoek richting te geven is het belangrijk om duidelijke onderzoeksvragen te stellen. Hier staan geen kant-en-klare onderzoeksvragen, maar wel richtingen waarin je je onderzoek focus kan geven:
 * Hoe reproduceerbaar zijn de gemeten waarden van de sensor? 
 * Hoe vergelijkbaar zijn de gemeten waarden van de sensor ten opzichte van dezelfde sensoren, maar ook de sensoren uit andere meetnetwerken?
 * Hoe variabel is de fijnstofconcentratie rond een (drukke) weg?
 * Hoe schoon is de lucht op school?
 * Welke blootstelling aan fijnstof krijg je onderweg van huis naar school, en is die elke dag hetzelfde?  

# Sensor
De fijnstof sensor [Sensirion SPS30](https://sensirion.com/products/catalog/SPS30) maakt met behulp van een laser het mogelijk de hoeveelheid deeltjes met een bepaalde grote te tellen. Deze waarden worden dan omgezet in massa fijnstof per volume ($\mu$g/m$^3$). De sensor kan ook andere waarden weergeven, maar voor nu laten we het bij de massa per volume. Als je de handleiding van de sensor goed doorleest zie je zelfs dat de sensor de PM4.0 en PM10 waarden niet meet, maar aan de hand van de andere waarden berekent. De nauwkeurigheid is welke spreiding de sensor mag aangeven bij het meten van dezelfde concentratie. Heb je meerdere sensoren dan kan je bij dezelfde blootstelling, binnen deze grenzen, meetwaarden verwachten. 

De sensor geeft de volgende waarden terug:

-------------------------------------------------------------
| naam  | grootte bereik    | nauwkeurigheid                |
-------------------------------------------------------------
| PM1.0 | $0.3 - 1.0 \mu$m  | 5$\mu$g/m$^3$ + 5% meetwaarde |
| PM2.5 | $0.3 - 2.5 \mu$m  | 5$\mu$g/m$^3$ + 5% meetwaarde |
| PM4.0 | $0.3 - 4.0 \mu$m  | 25$\mu$g/m$^3$                |
| PM10  | $0.3 - 10.0 \mu$m | 25$\mu$g/m$^3$                |
-------------------------------------------------------------

## Aansluiting
De sensor moet via de 5V aansluiting van de Raspberry Pi Pico aangesloten worden. Met de groene kant onder en kijken naar de sensor ziet de zijkant er zo uit:
```
 ---------------
 |       12345 |
 | *  *   *  * |
 ---------------
```
Pin 1 tot en met 5 zijn dan:
1. VDD (5V)
2. SDA
3. SCL
4. GND (for I2C)
5. GND

Pin 4 moet net als pin 5 met de GND verbonden zijn om de I2C aansluiting van de sensor te gebruiken. 

## Gebruik
When the sensor starts (`sps30.start_meaurement`) the fan will run for 10 seconds at maximum power to clean the device.

In the `main.py` file the sensor writes the measurement data to the serial port. In Thonny it will display the data on screen.

