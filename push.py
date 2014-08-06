#!/usr/bin/env python
import subprocess
import os 

# use these for coloring your text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cmd(cmd):
	os.system(cmd)

# commands to excecute 
cmd('clear')
print bcolors.BOLD + "Github Update Script" + bcolors.ENDC
comment = raw_input(bcolors.OKGREEN + "Type your update comment: " + bcolors.ENDC)				
cmd('git add *')
cmd('git add -u')			
cmd('git status')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
print bcolors.WARNING + "Update Complete!" + bcolors.ENDC