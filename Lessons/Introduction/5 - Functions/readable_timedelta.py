'''
https://classroom.udacity.com/courses/ud1110/lessons/49912e64-4fe1-4f06-8679-d17d4ad33969/concepts/3487f6f7-ff59-40cf-8746-106c6bdca7a5
'''


# write your function here
def readable_timedelta(days):
    weeks = days // 7
    days = days % 7
    return "{} week(s) and {} day(s).".format(weeks, days)


# test your function
print(readable_timedelta(1))
