#!/usr/bin/env python
'''
This script is just a proving-ground 
for automating RS-232 outputs
						- glennlopez
'''
import subprocess
import os 

# Text colors:
class colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# CMD FUNCTION - for running shell scripts using python | too lazy to code in #!/bin/bash
def cmd(cmd):
	os.system(cmd)


##########################
# COMMANDS TO EXECUTE
##########################

# Pre-config routine & checks
cmd("clear")
print colors.BOLD + 'Open serial ports are:' + colors.WHITE
cmd("dmesg | grep tty")
print ""

# Port setting
cmd("stty -F /dev/cu.usbserial-A700dYoR raw speed 9600")

# Stuff to send
cmd("echo 'Hello' > /dev/cu.usbserial-A700dYoR")