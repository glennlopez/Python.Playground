import calendar


class UserData:
    def __init__(self, user_name, reserved, use_date, comp_name, start_time, end_time, total_time):
        # raw data frames
        self.name = user_name
        self.reserved = reserved
        self.comp = comp_name

        # sub-classes
        self.time = self.Time(start_time, end_time, total_time)
        self.date = self.Date(use_date)

    class Date:
        def __init__(self, use_date):
            # raw data frames
            self.full = use_date

            # sugar for data sub-class
            self.day = self.get_day(1)
            self.month = self.get_month(1)

        def get_day(self, date_format=0):
            """
            Converts date string to day of the week
            :param date_format: 0 - default <int>, 1 - full <str>, 2 - Three letter <str>
            :return: day of the week
            """
            if date_format == 0:  # default value
                return calendar.weekday(int(tuple(self.full.split('/'))[2]), int(tuple(self.full.split('/'))[1]),
                                        int(tuple(self.full.split('/'))[0]))
            if date_format == 1:
                day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                return day[calendar.weekday(int(tuple(self.full.split('/'))[2]), int(tuple(self.full.split('/'))[1]),
                                            int(tuple(self.full.split('/'))[0]))]
            if date_format == 2:
                day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                return day[calendar.weekday(int(tuple(self.full.split('/'))[2]), int(tuple(self.full.split('/'))[1]),
                                            int(tuple(self.full.split('/'))[0]))]

        def get_month(self, date_format=0):
            """
            Converts date string to month<str>
            :param date_format: 0 - default <int>, 1 - full <str>, 2 - Three letter <str>
            :return: month value starting at 0/January
            """
            if date_format == 0:
                return int(tuple(self.full.split('/'))[1]) - 1

            if date_format == 1:
                month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                         'October', 'November', 'December']
                return month[int(tuple(self.full.split('/'))[1]) - 1]

            if date_format == 2:
                month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                         'Oct', 'Nov', 'Dec']
                return month[int(tuple(self.full.split('/'))[1]) - 1]

    class Time:
        def __init__(self, start_time, end_time, total_time):
            # raw data frames
            self.start_time = start_time
            self.end_time = end_time
            self.total_time = total_time

            # sugar for data sub-class
            self.start = self.get_start_time()
            self.end = self.get_end_time()
            self.total = self.get_total_time()



        def get_start_time(self, time=0):
            """
            Converts start_time <str> to usable <int> format
            :param time: type of time to return / all, hour, min, sec
            :return: Tuple of <int> if 0, else <int>
            """
            if time == 0:
                return (int(tuple(self.start_time.split(':'))[0]), int(tuple(self.start_time.split(':'))[1]),
                        int(tuple(self.start_time.split(':'))[2]))
            # below is redundant due to tuple above but kept for legacy support
            if time == 1 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
                return int(tuple(self.start_time.split(':'))[0])
            if time == 2 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
                return int(tuple(self.start_time.split(':'))[1])
            if time == 3 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
                return int(tuple(self.start_time.split(':'))[2])

        def get_end_time(self, time=0):
            """
            Converts end_time <str> to usable <int> format
            :param time: type of time to return / all, hour, min, sec
            :return: Tuple of <int> if 0, else <int>
            """
            if time == 0:
                return (int(tuple(self.end_time.split(':'))[0]), int(tuple(self.end_time.split(':'))[1]),
                        int(tuple(self.end_time.split(':'))[2]))
            # below is redundant due to tuple above but kept for legacy support
            if time == 1 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
                return int(tuple(self.end_time.split(':'))[0])
            if time == 2 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
                return int(tuple(self.end_time.split(':'))[1])
            if time == 3 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
                return int(tuple(self.end_time.split(':'))[2])

        def get_total_time(self, time=0):
            """
            Converts total_time <str> to usable <int> format
            :param time: type of time to return / all, hour, min, sec
            :return: Tuple of <int> if 0, else <int>
            """
            if time == 0:
                return (int(tuple(self.total_time.split(':'))[0]), int(tuple(self.total_time.split(':'))[1]),
                        int(tuple(self.total_time.split(':'))[2]))
            # below is redundant due to tuple above but kept for legacy support
            if time == 1 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
                return int(tuple(self.total_time.split(':'))[0])
            if time == 2 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
                return int(tuple(self.total_time.split(':'))[1])
            if time == 3 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
                return int(tuple(self.total_time.split(':'))[2])


def parse_csv(csv_file):
    """
    Takes a csv file and parses the data<str> into a list of tuples
    :param csv_file: .csv file to extract data from
    :return: list<L> of tuples
    """
    # open and parse csv file
    with open(csv_file, 'r') as data:
        log_data = data.read()
    log_row = log_data.split("\n")

    # return parsed csv using list comprehension as a list of tuples
    return [(tuple(log_row[element].split(','))) for element in range(len(log_row))]


# place csv data into a variable
log_entries = parse_csv('test.csv')

# print log_entry list
for i in range(len(log_entries)):
    print(log_entries[i])

print()
print()

usr00 = UserData(log_entries[0][0], log_entries[0][1], log_entries[0][2],
                 log_entries[0][3], log_entries[0][4], log_entries[0][5],
                 log_entries[0][6])

usr01 = UserData(log_entries[1][0], log_entries[1][1], log_entries[1][2],
                 log_entries[1][3], log_entries[1][4], log_entries[1][5],
                 log_entries[1][6])

print(usr00.time.start, type(usr00.time.start))
print(usr00.time.end, type(usr00.time.end))
print(usr00.time.total, type(usr00.time.total))
print(usr00.date.month)
