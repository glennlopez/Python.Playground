#!/usr/bin/env python
import subprocess			# Subprocess for Shell CMD
import os 					# OS Library

'''
This wraps up all subject outputs into one nice file 
'''

# SUBJECT NAMER
sub1 = 'subject_1'
sub1 = sub1.upper()


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
cmd('clear')

# OUTPUT
print (colors.BOLD + 'Grade Report' + colors.WHITE)
print ('[1] Subject 1')
print ('[2] Subject 2')
print ('[3] Subject 3')
print ('-----------------')
print
print 


# PROMPT
sel_action = input('Make a selection: ')

    # SELECTION 1
if sel_action == 1:
    cmd('clear')
    print colors.GREEN + sub1 + colors.WHITE
    sub1 = sub1.lower()
    cmd('python ' + sub1 + '/start.py')
    cmd('python ' + sub1 + '/editor.py')
