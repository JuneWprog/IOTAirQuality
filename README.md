# IOTAirQuality
<h3>[OverView]</h3>
                        <p>- Connected the SGP30 gas sensor, Adafruit 14 segment display and Beaglebone Black board on an I2C bus network </p>
                        <p>- Developed python program run in linux OS on BB board.</p>
                        <p>- The Python script enables Beaglebone Black  to read indexes from SGP30 and send data to 14 segment display </p>
                        <h3>[Project Goals]</h3>
                        <p>- The main goal of the project was to connect chips on a I2C bus network. </p>
                        <p>- Read 2 Air Quality Indexs: Total Volatile Organic Compounds (TVOCs) and Carbon dioxide (CO2) in real time.</p>
                        <p>- Display indexes on 14 segment Display accurately.</p>
                        <p>- Switch displaying index on CLI</p>
                        <h3>[project environment]</h3>
                        Ubuntu, python, Beaglebone Board
                        
#Shell command for detecting the attached devices:
I2cdetect -r 2
SGP30 address: 0x58
14-Segment-Display: 0x70

#Python Scripts:
1) displayv4.py 
Usage: python displayv4.py 123.4
❏	This program is used for displaying numbers and characters on Adafruit 14 segment LCD display. 
❏	The range of numbers that the program can display is 0.000-99999. For strings, it displays the first 4 characters or digits, the rest will be discarded. It can display decimal numbers in the following format: 1.234 12.34 123.4 1234.

2) gasdemo.py
Usage: python gasdemo.py [-t] [-c]
-c: display CO2 level in unit ppm 
-t: display TVOCs level 
❏	This program is used for reading air quality indexes from SGP30 gas sensor, parsing the data and then sending data onto a 14-segment LCD display. 
❏	It utilizes i2cset shell command to control the 14 segment display. 
❏	When displaying CO2 level, if the level is less than 2000 ppm, the display is stable.  When CO2 level is at 2000-5000 ppm, the display blinks slowly at a rate of 1Hz. When CO2 level is greater than 5000ppm, the display blinks faster at a rate of 2Hz. 

