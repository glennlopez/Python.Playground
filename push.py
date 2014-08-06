#!/usr/bin/env python
import subprocess
import os 

red='\e[0;31m'
NC='\e[0m' # No Color

def cmd(cmd):
	os.system(cmd)

comment = raw_input("Type Comment: ")
cmd('clear')				
cmd('git add *')			
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
cmd('${red}echo Push Script Complete!${NC}')