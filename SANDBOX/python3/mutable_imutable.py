"""
https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/201ed843-7285-4a46-807e-fd18f96cd7fe
"""

# python list are mutable
scores = ["A", "B", "B+", "C+"]
grades = ["C+", "A", "D", "F-"]

# make grades list point to scores list
grades = scores

# change letter grade in grade list WILL reflect to scores list
grades[0] = "C"


print("scores: " + str(scores))
print("scores: " + str(grades))






