# creating a set
myFruitSet = {'Apple', 'Orange', 'Apple', 'Grapes', 'Pineapple'}
myOddSet = set([1, 3, 5, 7, 9])
myEvenSet = set([2, 4, 6, 8, 10])
myRandNum = {3, 4, 1, 2, 7}
print(myFruitSet)
print(myOddSet)
print(myEvenSet)
print()

#testing intersection
print(myOddSet.union(myEvenSet))
print(myOddSet.intersection(myEvenSet))
print(myRandNum.intersection(myEvenSet))
print(myEvenSet|myOddSet)
print(myEvenSet.difference(myOddSet))
