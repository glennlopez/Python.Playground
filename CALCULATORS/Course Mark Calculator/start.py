#!/usr/bin/env python
from data_lib import *		# Database
from main import *			# Function Library

print subj_1['homework']
print average(subj_1['homework'])
print
print subj_1['quizzes']
print average(subj_1['quizzes'])
print
print subj_1['tests']
print average(subj_1['quizzes'])
print
print get_average(subj_1)

'''
hmw_wght = 0.1		#homework weight
qzz_wght = 0.3		#quizzes weight
tst_wght = 0.6		#tests wieght
'''
