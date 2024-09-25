# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain
import time
import datetime
import requests
import json
import settings as settings

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
cpuInfo = segments.Seg7x4(i2c, address=0x74)
cpuInfo.brightness = 0.4

# Clear the displays
localTime.fill(0)
cpuInfo.fill(0)

while True:

    # get current local time
    now = datetime.datetime.now()
    currentTime = now.strftime("%I:%M")

    # Display the local time
    localTime.print(currentTime)

    try:
        # Get CPU info from the dashboard
        response = requests.get("https://" + settings.dashboardURL + "/computer")

        data = json.loads(json.loads(response.json()["message"])["HTML"])
        cpu_percent = float(data["cpu_percent"])

        # Format CPU percentage as string with leading spaces and one decimal place
        cpu_display = f"{cpu_percent:.1f}".rjust(5)

        # Display the CPU percentage
        cpuInfo.print(cpu_display)
    except Exception as e:
        print(f"Error fetching CPU info: {e}")
        cpuInfo.print("ERR")

    time.sleep(5)
