#!/usr/bin/env python
semi = {
    "name": "Semiconductor",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
phys = {
    "name": "Physics",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
garb = {
    "name": "Garbage",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# FUNCTION - Course  Weight
hmw = 0.1
qzz = 0.3
tst = 0.6

# FUNCTION - Mark Average Calculation
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total/len(numbers)
    return total
  
# FUNCTION - Subject Average Calculation  
def get_average(subject):
    homework = average(subject["homework"])
    quizzes = average(subject["quizzes"])
    tests = average(subject["tests"])
    return homework*hmw + quizzes*qzz + tests*tst

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

#debug script
classes = semi,
classes = get_course_standing(classes)
classes = int(classes)
print classes

    
    
