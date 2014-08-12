#!/usr/bin/env python
from data_lib import *		# Database
from main import *

#CALCULATIONS
avg_subj_1 = get_average(subj_1)
avg_hmw = average(subj_1['homework'])
avg_qzz = average(subj_1['quizzes'])
avg_tst = average(subj_1['tests'])

#OUTPUTS
print (avg_subj_1)
