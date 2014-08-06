#!/usr/bin/env python
import subprocess
import os 

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
print 'Pushing commits to Github...'
comment = raw_input("Type git-commit comment: ")				
cmd('git add *')			
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
cmd('echo Push Script Complete!')
print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC