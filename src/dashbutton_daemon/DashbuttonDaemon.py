# -*- coding: utf-8 -*-
"""Dashbutton daemon

Once started this module acts as daemon in the background and waits for
a pushed dashbutton to trigger a callback method. 
"""

__author__     = "Dennis Jung"
__copyright__  = "Copyright 2018, Dennis Jung"
__credits__    = ["Dennis Jung"]
__license__    = "GPL Version 3"
__maintainer__ = "Dennis Jung"
__email__      = "Dennis.Jung@it-jung.com"


#===============================================================================
# Additional information
#===============================================================================


#===============================================================================
# Imports
#===============================================================================
import logging
import argparse
from scapy.all import *
import time


#===============================================================================
# Evaluate parameters
#===============================================================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--v1', 
                        help='Debug level INFO', 
                        dest='verbose_INFO',
                        default=False,
                        action='store_true')
    parser.add_argument('--v2', 
                        help='Debug level ERROR', 
                        dest='verbose_ERROR',
                        default=False,
                        action='store_true')
    parser.add_argument('--v3', 
                        help='Debug level DEBUG', 
                        dest='verbose_DEBUG',
                        default=False,
                        action='store_true')
        
    args = parser.parse_args()


#===============================================================================
# Setup logger
#===============================================================================
if __name__ == '__main__':
    log_level = logging.CRITICAL
    
    if args.verbose_INFO: log_level = logging.INFO
    if args.verbose_ERROR: log_level = logging.ERROR
    if args.verbose_DEBUG: log_level = logging.DEBUG
    
#    logging.basicConfig(level=log_level,
#                        format="[{asctime}] - [{levelname}] - [{process}:{thread}] - [{filename}:{funcName}():{lineno}]: {message}",
#                        datefmt="%Y-%m-%d %H:%M:%S",
#                        style="{")

    logging.basicConfig(level=log_level,
                        format="[{asctime}] - [{levelname}]: {message}",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        style="{")
        
logger = logging.getLogger(__name__)


#===============================================================================
# Constant declarations
#===============================================================================
DASH_BUTTONS = {"6C:56:97:55:96:CD" : "First_Dashbutton",
                "6C:56:97:17:2A:BE" : "Second_Dashbutton"} # HW MAC must be in upper case


#===============================================================================
# Method definitions
#===============================================================================
def arp_pkt(pkt):
        if ARP in pkt:
            if pkt[ARP].op == 1:
                    mac = pkt[ARP].hwsrc.upper()
                    
                    if (mac in DASH_BUTTONS):
                        button_pressed(DASH_BUTTONS[mac])


def button_pressed(button):
    global now_ts
    global button1_ts
    global button2_ts
    
    now_ts = time.time()
    
    if ((button == "First_Dashbutton") and (now_ts - button1_ts > 5)):
        button1_ts = now_ts
        
        print('First dashbutton was pushed')
    elif ((button == "Second_Dashbutton") and (now_ts - button2_ts > 5)):
        button2_ts = now_ts
        
        print('Second dashbutton was pushed')
    else:
        pass
    

#===============================================================================
# Class definitions
#===============================================================================
    
    
#===============================================================================
# Start of program
#===============================================================================
now_ts = time.time()    # Initialize current timestamp
button1_ts = now_ts - 5 # Initialize timestamp for the first dashbutton
button2_ts = now_ts - 5 # Initialize timestamp for the second dashbutton


def main():
    sniff(prn=arp_pkt, filter="arp", store=0, count=0)
    
    
if __name__ == '__main__':
    main()