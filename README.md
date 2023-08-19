# Office Wall Multiclock - Temperature / 
Using this magic candle, you can tell the current temperature and conditions outside instantly

![Finished](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/7.png)

#### Flashing RaspberriPi Hard Disk / Install Required Software (Using Ubuntu Linux)

Download "RASPBIAN"
https://www.raspberrypi.org/downloads/raspbian/

**Create your new hard disk for DashboardPI**
>Insert the microSD to your computer via USB adapter and create the disk image using the `dd` command
>
> Locate your inserted microSD card via the `df -h` command, unmount it and create the disk image with the disk copy `dd` command
>
> $ `df -h`
> */dev/sdb1       7.4G   32K  7.4G   1% /media/XXX/1234-5678*
>
> $ `umount /dev/sdb1`
>
> **Caution: be sure the command is completely accurate, you can damage other disks with this command**
>
> *if=location of RASPBIAN image file*
> *of=location of your microSD card*
>
> $ `sudo dd bs=4M if=/path/to/raspbian-lite.img of=/dev/sdb`
> *(note: in this case, it's /dev/sdb, /dev/sdb1 was an existing factory partition on the microSD)*

**Setting up your RaspberriPi**

*Insert your new microSD card to the raspberrypi and power it on with a monitor connected to the HDMI port*

Login
> user: **pi**
> pass: **raspberry**

Change your account password for security
>`sudo passwd pi`

Enable RaspberriPi Advanced Options
>`sudo raspi-config`

Choose:
`1 Expand File System`

`9 Advanced Options`
>`A2 Hostname`
>*change it to "OfficeMultiClock"*
>
>`A4 SSH`
>*Enable SSH Server*
>
>`A7 I2C`
>*Enable i2c interface*

**Enable the English/US Keyboard**

>`sudo nano /etc/default/keyboard`

> Change the following line:
>`XKBLAYOUT="us"`

**Reboot PI for Keyboard layout changes / file system resizing to take effect**
>$ `sudo shutdown -r now`

**Auto-Connect to your WiFi**

>`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

Add the following lines to have your raspberrypi automatically connect to your home WiFi
*(if your wireless network is named "linksys" for example, in the following example)*

	network={
	   ssid="linksys"
	   psk="WIRELESS PASSWORD HERE"
	}

**Reboot PI to connect to WiFi network**

>$ `sudo shutdown -r now`
>
>Now that your PI is finally on the local network, you can login remotely to it via SSH.
>But first you need to get the IP address it currently has.
>
>$ `ifconfig`
>*Look for "inet addr: 192.168.XXX.XXX" in the following command's output for your PI's IP Address*

**Go to another machine and login to your raspberrypi via ssh**

> $ `ssh pi@192.168.XXX.XXX`

**Start Installing required packages**

>$ `sudo apt-get update`
>
>$ `sudo apt-get upgrade`
>
>$ `sudo apt-get install memcached vim git python-smbus i2c-tools python-imaging python-smbus build-essential python-dev rpi.gpio python3 python3-pip python-memcache`

**Update local timezone settings

>$ `sudo dpkg-reconfigure tzdata`

`select your timezone using the interface`

**Setup the simple directory `l` command [optional]**

>`vi ~/.bashrc`
>
>*add the following line:*
>
>`alias l='ls -lh'`
>
>`source ~/.bashrc`

**Fix VIM default syntax highlighting [optional]**

>`sudo vi  /etc/vim/vimrc`
>
>uncomment the following line:
>
>_syntax on_

# Supplies Needed

**RaspberryPi Zero**

![RaspberryPi Zero](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/PiZero.jpg)

**USB WIFI (if not a PiZero W)**

![USB WIFI (if not a PiZero W)](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/wifi.jpg)

**7 Segment Display (x4)**

![7 Segment Display (x4)](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/7segment.png)

**DHT22**

![DHT22](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/DHT22.png)

**14 Segment Display (x4)**

![14 Segment Display (x4)](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/alphanum.png)

**7x14" Frame**

![7x14" Frame](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/frame.png)

**Semi-Transparent PlexiGlass**

![Semi-Transparent PlexiGlass](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/glass.png)


# Building the OfficeMultiClock

## Solder Unique Display Jumpers
*NOTE: All the I2C backpacks must be soldered on the back of each of the displays, the backpacks come with the display and must all be soldered on first.*

For each of the I2C backpack displays you must solder the jumpers on the back in the **all the possible combinations** to have your RaspberriPI I2C interface to recognize each display with a **unique address**.  

Leave the first display with no jumper soldered, the 2nd with the farthest right soldered, the 3rd with only the middle soldered and so on...  Eventually you'll have to solder jumpers in all the combinations of 2 at a time connected and the final display with all 3 jumpers soldered to be connected.

*There's a total of 3 pins so you should have a total combination of 8 unique combinations.*

![Solder Unique Display Jumpers](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/displays.jpg "Solder Unique Display Jumpers")

### Wiring the Components

Each of the 14 segment alpha numeric displays needs to have a connection to the RaspberryPI GND, 5V and 3V pins.  The 7 segment display only needs connectivity to the GND and 5V pins.

![Wiring Diagram](https://raw.githubusercontent.com/khinds10/OfficeMultiClock/master/construction/wiring-diagram.png "Wiring Diagram")

I've used standard jumper wires to connect to all the pins on the display / RaspberryPI pins and grouped the common connections (all the GND wires, 5V wires) with a wirenut.

For each display in the dashboard ALL of the D and C pins need to be connected to the SCL and SDA pins on the PI.

### Set pi user crontab 

`$ crontab -e`

`*/1 * * * * python /home/pi/OfficeMultiClock/XXX.py`

### Set root user crontab (this library requires root access)

Set "on reboot" to run the candle python script forever

`$ sudo su`

`$ crontab -e`

`@reboot python XXX`

# Finished!
