import calendar


class UserData:
    def __init__(self, user_name, reserved, use_date, comp_name, start_time, end_time, total_time):
        # raw data frames
        self.name = user_name
        self.reserved = reserved
        self.date = use_date
        self.comp = comp_name
        self.start = start_time
        self.end = end_time
        self.total = total_time

        # sugar for data class
        self.user = self.get_name()
        self.day = self.get_day(1)
        self.month = self.get_month(1)

    def get_day(self, date_format=0):
        """
        Converts date string to day of the week
        :param date_format: 0 - default <int>, 1 - full <str>, 2 - Three letter <str>
        :return: day of the week
        """
        if date_format == 0:  # default value
            return calendar.weekday(int(tuple(self.date.split('/'))[2]), int(tuple(self.date.split('/'))[1]),
                                    int(tuple(self.date.split('/'))[0]))
        if date_format == 1:
            day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            return day[calendar.weekday(int(tuple(self.date.split('/'))[2]), int(tuple(self.date.split('/'))[1]),
                                        int(tuple(self.date.split('/'))[0]))]
        if date_format == 2:
            day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            return day[calendar.weekday(int(tuple(self.date.split('/'))[2]), int(tuple(self.date.split('/'))[1]),
                                        int(tuple(self.date.split('/'))[0]))]

    def get_month(self, date_format=0):
        """
        Converts date string to month<str>
        :param date_format: 0 - default <int>, 1 - full <str>, 2 - Three letter <str>
        :return: month value starting at 0/January
        """
        if date_format == 0:
            return int(tuple(self.date.split('/'))[1]) - 1

        if date_format == 1:
            month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                     'October', 'November', 'December']
            return month[int(tuple(self.date.split('/'))[1]) - 1]

        if date_format == 2:
            month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                     'Oct', 'Nov', 'Dec']
            return month[int(tuple(self.date.split('/'))[1]) - 1]

    def get_start_time(self, time=0):
        """
        Converts start_time time<str> to hour<int>, min<int>, sec<int>
        :param time: type of data to return (hour, min, sec)
        :return: int
        """
        if time == 0 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
            return int(tuple(self.start.split(':'))[0])
        if time == 1 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
            return int(tuple(self.start.split(':'))[1])
        if time == 2 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
            return int(tuple(self.start.split(':'))[2])

    def get_end_time(self, time=0):
        """
        Converts total_time time<str> to hour<int>, min<int>, sec<int>
        :param time: type of data to return (hour, min, sec)
        :return: int
        """
        if time == 0 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
            return int(tuple(self.end.split(':'))[0])
        if time == 1 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
            return int(tuple(self.end.split(':'))[1])
        if time == 2 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
            return int(tuple(self.end.split(':'))[2])

    def get_total_time(self, time=0):
        """
        Converts end_time time<str> to hour<int>, min<int>, sec<int>
        :param time: type of data to return (hour, min, sec)
        :return: int
        """
        if time == 0 or time == 'h' or time == 'hh' or time == 'hrs' or time == 'hour' or time == 'hours':
            return int(tuple(self.total.split(':'))[0])
        if time == 1 or time == 'm' or time == 'mm' or time == 'min' or time == 'minute' or time == 'minutes':
            return int(tuple(self.total.split(':'))[1])
        if time == 2 or time == 's' or time == 'ss' or time == 'sec' or time == 'second' or time == 'seconds':
            return int(tuple(self.total.split(':'))[2])

    def get_name(self):
        """
        Cleans up user_name from Data-frame incase it's been formated incorrectly
        :return: string
        """
        return self.name.title()


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

# print debug
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

print(usr00.name, type(usr00.name))
print(usr00.user, type(usr00.user))
print(usr00.month, type(usr00.month))
print(usr00.get_start_time(), type(usr00.get_start_time()))
print(usr00.get_total_time('second'), type(usr00.get_total_time('s')))
