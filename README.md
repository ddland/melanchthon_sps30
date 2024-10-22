# Melanchthon en Fijnstof
Het meten van fijnstof kan inzichtelijk maken hoe schoon de lucht in je omgeving is. Er zijn wereldwijd richtlijnen voor de maximale fijnstof concentratie waar je aan blootgesteld zou mogen worden. Voor fijnstof heeft de [WHO](https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health) de volgende AQG levels (air-quality-guidelines) voorgeschreven:

PM | gemiddelde over | AQG  
---|-----------------|----------
PM2.5 | jaarlijks | 5 ug/m^3 
PM2.5 | 24 uur    | 15 ug/m^3
PM10  | jaarlijks | 15 ug/m^3
PM10  | 24 uur    | 45 ug/m^3

In [Nederland](https://www.infomil.nl/onderwerpen/landbouw/stof/handreiking-fijn-1/juridisch-kader/wettelijke-eisen/) zijn andere waarden als grenswaarden ingesteld:

|PM | gemiddelde over | AQG  |
|-----|----------------|---------|
|PM2.5 | jaarlijks | 25 ug/m^3  |
|PM10  | jaarlijks | 40 ug/m^3  |
|PM10  | 24 uur    | 50 ug/m^3 |

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


| naam  | grootte bereik    | nauwkeurigheid                |
--------|-------------------|-------------------------------|
| PM1.0 | 0.3 - 1.0 um  | 5 ug/m^3 + 5% meetwaarde |
| PM2.5 | 0.3 - 2.5 um  | 5 ug/m^3 + 5% meetwaarde |
| PM4.0 | 0.3 - 4.0 um  | 25 ug/m^3                |
| PM10  | 0.3 - 10.0 um | 25 ug/m^3                |

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
4. GND (voor I2C)
5. GND

Pin 4 moet net als pin 5 met de GND verbonden zijn om de I2C aansluiting van de sensor te gebruiken. 
De software om de sensor met een Raspberry Pi Pico uit te lezen staat in de lib directory van dit repositorie. In diezelfde directory staan ook bibliotheken die je kan gebruiken om een GPS sensor uit te lezen, of een OLED scherm aan te sturen. 

Voor gebruik moet de `melanchthon_sps30.py` en de `sps30.py` file naar de `lib` folder op de Raspberry Pi Pico geupload worden. Daarna kunnen de `sps_...py` files gebruikt worden, afhankelijk van de toepassing. 
Door deze files te hernoemen naar `main.py` worden ze bij opstarten van de Raspberry Pi Pico gelijk uitgevoerd. Op die manier is het mogelijk zonder computer in de buurt toch gebruik te maken van de sensor. 

Het bestand `melanchthon_sps30.py` is zo gemaakt dat deze alleen de PM1.0, PM2.5, PM4.0 en PM10 waarden teruggeeft. Daarnaast begint de sensor eerst met een schoonmaak routine zodra het bestand uitgevoerd wordt.

## Code
De bestanden (sps_xxx.py) maken op verschillende manieren gebruik van de sensor en geven de data weer. Van opslaan tot via de telefoon uitlezen, er zijn veel mogelijkheden. 
Wil je de sensor zonder computer (Thonny) gebruiken, dan moet de sps_xxx.py file hernoemd worden naar main.py (en alle afhankelijkheden moeten op de Raspberry Pi Pico in de lib folder staan), deze file wordt automatisch uitgevoerd als de Rasbperry Pi Pico van stroom voorzien wordt. Om data daarna van de Raspberry Pi Pico af te lezen moet die weer aangesloten worden op de computer om de bestanden van de microcontroller naar de computer te kopieren. 

### SPS print
Het bestand `sps_print.py` geeft de gemeten waarden weer op het scherm via Thonny of de serial port. 

### SPS save
Het bestand `sps_save.py` slaat de data gemeten door de sensor op. Opslag van de Raspberry Pi Pico is beperkt (er blijft ongeveer 1.5 Mb over na uploaden van de code) en moet dus regelmatig van de sensor gedownload worden. 

### SPS display
Het bestand `sps_display.py` geeft de gemeten waarden weer op een OLED scherm met de SSD1306 driver.

### SPS GPS
Het bestand `sps_gps.py` geeft de locatie en tijd naast de gemeten fijnstof concentratie weer op het scherm via Thonny of de serial port.

### SPS_webserver
De Raspberry Pi Pico start een access-point (`HHS-MELACHTHON`) waar je op kan inloggen met je computer of telefoon (password: 123456789). Daarna kan je naar de website: [192.168.4.1](http://192.168.4.1) gaan waar je de metingen kan uitvoeren (en aflezen). Data kan je kopieren van de website naar een logbestand, of je kan via andere tools (bijvoorbeeld een python scripts) automatisch elke paar seconden de data uitlezen.  
