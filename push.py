#!/usr/bin/env python
import subprocess
import os 

# text coloring format
class colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cmd(cmd):
	os.system(cmd)

# commands to excecute 
cmd('clear')
print colors.BOLD + "Github Update Script" + colors.WHITE
comment = raw_input(colors.GREEN + "Type your update comment: " + colors.WHITE)				
cmd('git add *') 	#updates changes made inside files
cmd('git add -u') 	#updated deleted files			
cmd('git status')	#displays changes to be pushed to github
cmd("git commit -m '"+comment+"'")
cmd('git push')		#push changes to github
print 
print colors.YELLOW + "Update Complete!" + colors.WHITE