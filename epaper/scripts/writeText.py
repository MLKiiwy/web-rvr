#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG)

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'node_modules/e-Paper/RaspberryPi&JetsonNano/python/pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'node_modules/e-Paper/RaspberryPi&JetsonNano/python/lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    logging.info("Write text on epd2in7b (e-paper 2.7 color screen)")
    
    epd = epd2in7b.EPD()
    logging.info("Send message", argv[1])
    epd.init()
    logging.info("Init done")
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRedimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
    
    drawblack = ImageDraw.Draw(HBlackimage)
    drawred = ImageDraw.Draw(HRedimage)
    drawblack.text((10, 0), sys.argv[1], font = font24, fill = 0)
    drawred.line((165, 50, 165, 100), fill = 0)
    drawred.line((140, 75, 190, 75), fill = 0)
    drawred.arc((140, 50, 190, 100), 0, 360, fill = 0)
    drawred.rectangle((80, 50, 130, 100), fill = 0)
    drawred.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
    logging.info("Display done")
    time.sleep(2)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7b.epdconfig.module_exit()
    exit()
