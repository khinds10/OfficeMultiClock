# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain
import time
import datetime
import pytz

# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# local time red 70
localTime = segments.Seg7x4(i2c, address=0x70)
localTime.brightness = 0.4

# remote time red 74
remoteTime = segments.Seg7x4(i2c, address=0x74)
remoteTime.brightness = 0.4

# Clear the displays
localTime.fill(0)
remoteTime.fill(0)

while True:

    # get current local time
    now = datetime.datetime.now()
    currentTime = now.strftime("%I:%M")

    # Get the current date and time in the timezone, Set the timezone
    timezone = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(timezone)
    indiaTime = now.strftime("%I:%M")

    # display the time
    localTime.print(currentTime)
    remoteTime.print(indiaTime)
    
    time.sleep(1)
