#!/usr/bin/env python
import subprocess
import os 

def cmd(cmd):
	os.system(cmd)
		#git add *
		#git status -s
		#git commit -m '<comment goes here>'
		#git push
comment = raw_input("Type Comment: ")
cmd('clear')				#clears terminal
cmd('git add *')			#adds changes
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
cmd('echo Push Script Complete!')