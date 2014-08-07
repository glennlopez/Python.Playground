#!/usr/bin/env python

#SUBJECT DATABASE
compsci = {
    "name": "Computer Science",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

#SUBJECT WIEGHT
hmw = 0.1
qzz = 0.3
tst = 0.6


#FUNCTION - Average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total/len(numbers)
    return total

#FUNCTION - Wieghed Average    
def get_average(subject):
    homework = average(subject["homework"])
    quizzes = average(subject["quizzes"])
    tests = average(subject["tests"])
    return homework*hmw + quizzes*qzz + tests*tst

'''
#FUNCTION - letter grade    
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
'''

#FUNCTION - Overall average standing
def get_overall_average(subjects):
    results = []
    for subject in subjects:
        results.append(get_average(subject))
    return average(results)

#OUTPUT
subjects = compsci
subjects = get_overall_average(subjects)
subjects = int(subjects)
print subjects

    
    
