#!/usr/bin/env python
from wght import *          # Used for displaying Marking Wieght

'''
This holds the functions used in start.py. Add functions you would
like to use here so other subjects can use the same file
'''

# FUNCTION - Mark Average Calculation
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total/len(numbers)
    return total
  
# FUNCTION - Subject Average Calculation  
#note: keep _wght isolated in subject folder (wieght changes per subject)
def get_average(subject):
    homework = average(subject["homework"])
    quizzes = average(subject["quizzes"])
    tests = average(subject["tests"])
    return homework*hmw_wght + quizzes*qzz_wght + tests*tst_wght

# FUNCTION - Grade Letter Equivalent   
def get_letter_grade(score):
    score = int(score)
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# FUNCTION - Overall Course Standing
def get_course_standing(classes):
    results = []
    for subject in classes:
        results.append(get_average(subject))
    return average(results)