#!/usr/bin/env python
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
 
def cmd(cmd):
	os.system(cmd)


# USER PROMPT
print (colors.WHITE + '--------------')
print
print ('[1] Add marks for Homework')
print ('[2] Add marks for Quiz')
print ('[3] Add marks for Test')
print (colors.YELLOW + '[X]' + colors.WHITE + ' Edit mark weight')
print (colors.RED + '[4]' + colors.WHITE + ' Go Back')
print
do_edit = input('Type your selection: ')

if do_edit == 1:
	cmd('nano subject_1/homework.txt')
