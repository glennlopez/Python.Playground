#!/usr/bin/env python
from data_lib import *		# Database
from main import *			# Function Library

#SUBJECT NAMES
subject_1 = "Subject 1"		# <--- Subject 1 Name
subject_2 = "Subject 2"		# <--- Subject 2 Name
subject_3 = "Subject 3"		# <--- Subject 3 Name
subject_4 = "Subject 4"		# <--- Subject 4 Name
subject_5 = "Subject 5"		# <--- Subject 5 Name
subject_6 = "Subject 6"		# <--- Subject 6 Name
subject_7 = "Subject 7"		# <--- Subject 7 Name

#CALCULATIONS
avg_subj_1 = get_average(subj_1)

#OUTPUTS
print "Your Average for '%s' so far is %s" %(subject_1, avg_subj_1)
