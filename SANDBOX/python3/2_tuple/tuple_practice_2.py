myTuple = (5, 'A', "Mars", False, "SpaceX", 'G')
myNumTup = (1,2,3,4,5,6,7,8,9,10)


#basic tuple
print("myTuple:" + str(myTuple))

#immutability test
# myTuple[1] = 'B'

#ordered test
print("Last item:", myTuple[-1])

#slicing test
print(myTuple[1:4])
print(myTuple[2:5])
print("Even index: ", myNumTup[1::2])
print("Odd index: ", myNumTup[::2])
print(max(myNumTup))