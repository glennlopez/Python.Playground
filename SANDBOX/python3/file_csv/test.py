import calendar


def parse_csv(csv_file):
    """
    Takes a csv file and parses the data into a list of tuples
    :param csv_file: .csv file to extract data from
    :return: list of tuples
    """
    # open and parse csv file
    with open(csv_file, 'r') as data:
        log_data = data.read()
    log_row = log_data.split("\n")

    # return parsed csv using list comprehension
    return [(tuple(log_row[element].split(','))) for element in range(len(log_row))]


def day_of_week(mmddyyy):
    '''
    Converts a date string formatted as mm/dd/yyyy and returns the day of the week as in integer
    :param mmddyyy: string of mm/dd/yyy
    :return: int - [M, T, W, T, F ,S ,S]
    '''
    return calendar.weekday(int(tuple(mmddyyy[2].split('/'))[2]), int(tuple(mmddyyy[2].split('/'))[0]),
                            int(tuple(mmddyyy[2].split('/'))[1]))


log_entries = parse_csv('test.csv')

# print debug
for i in range(len(log_entries)):
    print(log_entries[i])

print()
print()

print(log_entries[1][2])

# day of the week [m t w t f s s]
# print(calendar.weekday(int(tuple(log_entries[1][2].split('/'))[2]), int(tuple(log_entries[1][2].split('/'))[0]), int(tuple(log_entries[1][2].split('/'))[1])))


print(day_of_week(log_entries[0]))
