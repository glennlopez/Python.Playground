#!/usr/bin/env python
# Set minimum to the min value of any set of numbers on line 3
x = input("Type a number")
y = input("Type another number")
z = input("Type another, one last time")

numbers = (x, y, z)
minimum = min(numbers)
maximum = max(numbers)

peak = maximum - minimum

cubed = peak**3
divpi = cubed/3.14


print"The lowest number you typed was %s, which is %s numbers lower than your highest (%s). Cubing the peak (%s) gives us %s." %(minimum, peak, maximum, peak, cubed)

ask = raw_input("Would you like to divide your cubed peak by pi? (Type yes or no)")

asklower = ask.lower()

if asklower == 'yes':
    print "The number %s divide by pi is %s" %(cubed, divpi)
else:
    print "Ok, all done then!"


 