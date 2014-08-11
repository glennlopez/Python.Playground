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
cmd('clear')

# SUBJECT 1 - 
cmd('python subject_1/start.py')