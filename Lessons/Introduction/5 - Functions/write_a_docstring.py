def readable_timedelta(days):
    # insert your docstring here
    '''
    Converts days to Weeks + Days
    :param days: int
    :return: weeks and remainder days
    '''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)