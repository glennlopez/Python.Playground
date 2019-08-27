"""
https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/2aa94895-d620-4d00-9d91-43771844cdcf


Use list indexing to determine how many days are in a particular month based on the integer variable month,
and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31,
since the eighth month, August, has 31 days.

Remember to account for zero-based indexing!
"""

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
# - first attempt: num_days = days_in_month[month]
num_days = days_in_month[month - 1] # is -1 becuase array indexing starts at 0

print(num_days)