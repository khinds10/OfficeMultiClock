# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain
import time
import datetime
import json

# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

def padDigits(temp):
    if len(str(temp)) > 2:
        return " " + str(temp) + "F"
    else:
        return str(temp) + "F"

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# inside yellow 71
insideYellow = segments.Seg7x4(i2c, address=0x71)
insideYellow.brightness = 0.3

# outside green 72
outsideGreen = segments.Seg7x4(i2c, address=0x72)
outsideGreen.brightness = 1

# Clear the displays
insideYellow.fill(0)
outsideGreen.fill(0)

# get the values from weatherInfo to show as digits
with open('weatherInfo.json', 'r') as file:
    weatherInfo = json.load(file)

insideYellow.print(padDigits(weatherInfo['insideTemperature']))
outsideGreen.print(padDigits(weatherInfo['apparentTemperature']))
