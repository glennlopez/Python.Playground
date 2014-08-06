#!/usr/bin/env python
import subprocess
def bash(cmd):
	subprocess.check_call(cmd)
	

ls_prompt = raw_input("Would you like to list curent files and folders in the directory? [Y/N] ")
ls_prompt = ls_prompt.lower()
if ls_prompt =='yes' or ls_prompt == 'y' or ls_prompt == 'ye':
	print
	print
	bash('ls')
	print
	print "IT IS DONE!"
else:
	print "NOTHING EXECUTED - user typed: %s" %(ls_prompt)
	print 
clear_prompt = raw_input("Clear the terminal? [Y/N]")
clear_prompt = clear_prompt.lower()
if clear_prompt == 'yes' or clear_prompt == 'y' or ls_prompt == 'ye':
	print
	print
	#subprocess.check_call(["clear"])
	bash('clear')
	next_ins = raw_input("What would you like to do next? ")
else:
	next_ins = raw_input("What would you like to do next? ")

if next_ins == "nothing":
	print "exiting terminal..."

