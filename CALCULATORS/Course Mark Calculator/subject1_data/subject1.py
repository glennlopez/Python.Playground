#!/usr/bin/env python
#from test import * 			#imports data from test.py
from homework import * 		#imports data from homework.py
from quiz import *			#imports data from quiz.py
from wieght import *		#imports subject wieght
from main import *			#imports Calculation function

test = open("test.txt", "r")
print test.read()

homework()
quiz()
wieght()
main()