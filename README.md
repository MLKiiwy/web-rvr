# web-rvr

## Install

Use rapbian https://www.raspberrypi.org/downloads/raspbian/
Don't use lite version, because we want a screen for debug

### Add ssh + wifi configuration

On boot partition add `ssh` file.
Also on boot partition add `wpa_supplicant.conf` file **filled**
See https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

After that **run it**, find it on the network for getting the ip.


## Install 3.5 inch screen

I try to follow: https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(A)
It's still not working (white screen)
Same with https://github.com/goodtft/LCD-show

No idea how to make it work for now.

## Install e-ink screen

Wiki: https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT#Raspberry_Pi

### Requirements

Should already by part of raspbian, but you can try:
```bash
sudo apt-get install python-dev python-pil python-imaging
sudo apt-get install python-smbus python-serial
sudo pip install spidev
```

### Demo

Execute:
```bash
git clone https://github.com/waveshare/e-Paper
cd e-Paper/RaspberryPi\&JetsonNano/python/examples
sudo python epd_2in7_test.py
# For colors
sudo python epd_2in7b_test.py
```

You should see lot of different images on the screen.

## Saved image

- raspbian_with_wifi_23_11_2019

Simply raspbian with Wifi config and ssh enabled.
User: pi/raspberry

