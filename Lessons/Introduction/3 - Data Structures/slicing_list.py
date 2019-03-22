"""
Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/201ed843-7285-4a46-807e-fd18f96cd7fe
"""

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
recent_date = [eclipse_dates[-3], eclipse_dates[-2], eclipse_dates[-1]]
print(recent_date)

# OR

print(eclipse_dates[-3:])