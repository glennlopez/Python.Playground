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


def cmd(cmd):
	os.system(cmd)

cmd('clear')
print bcolors.OKGREEN + "Github Update Script" + bcolors.ENDC
comment = raw_input("Type your update comment: ")				
cmd('git add *')			
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
print bcolors.WARNING + "Update Complete!" + bcolors.ENDC