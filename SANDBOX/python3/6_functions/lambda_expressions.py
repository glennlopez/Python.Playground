# standard defined function
def square_area(l, h):
    '''
    Calculates Area of a square
    :param l:
    :param h:
    :return:
    '''
    return l * h


# lambda equivalent
sqr_area = lambda l, h: l * h
full_name = lambda fn = input("First name: "), ln = input("Last Name: "): print('Hello {} {}'.format(fn, ln))

print(square_area(3, 3))
print(sqr_area(3, 3))
full_name()

