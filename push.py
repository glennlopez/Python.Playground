#!/usr/bin/env python
import subprocess
import os 

# use these for coloring your text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cmd(cmd):
	os.system(cmd)

# commands to excecute 
cmd('clear')
print bcolors.BOLD + "Github Update Script" + bcolors.ENDC
comment = raw_input(bcolors.GREEN + "Type your update comment: " + bcolors.ENDC)				
cmd('git add *') 	#updates changes made inside files
cmd('git add -u') 	#updated deleted files			
cmd('git status')	#displays changes to be pushed to github
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
print bcolors.YELLOW + "Update Complete!" + bcolors.ENDC