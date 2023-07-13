# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

import time
import datetime

# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
display1 = segments.Seg14x4(i2c, address=0x77)
display2 = segments.Seg14x4(i2c, address=0x76)
display3 = segments.Seg14x4(i2c, address=0x75)
display4 = segments.Seg14x4(i2c, address=0x73)

# Clear the display.
display1.fill(0)
display1.brightness = 0.25

display2.fill(0)
display2.brightness = 0.25

display3.fill(0)
display3.brightness = 0.25

display4.fill(0)
display4.brightness = 0.25

now = datetime.datetime.now()
dateString = now.strftime("%a %b %d")
    
suffix = 'th'
if dateString.endswith('1') and not dateString.endswith('11'):
    suffix = 'st'
elif dateString.endswith('2') and not dateString.endswith('12'):
    suffix = 'nd'
elif dateString.endswith('3') and not dateString.endswith('13'):
    suffix = 'rd'

dateString = dateString.upper() + suffix
dateString += now.strftime("%Y")
substrings = [dateString[i:i+4] for i in range(0, len(dateString), 4)]

display1.print(substrings[0])
display2.print(substrings[1])
display3.print(substrings[2])
display4.print(substrings[3])
