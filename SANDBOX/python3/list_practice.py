#regular list
animals = ['Dog', 'Cat', 'Horse', 'Bird']
print("List:", animals)
print("animal[0]:", animals[0])
print()

#mixed list
'''
Lists in python can be mixed data types. 
Grouping int and string and bool in one datatype 
without specifying the datatype like structs in C
'''
pandoraBox = [3.14, "Math", 'A', 7, True, -123567847337377457475757558686757567448585848585]
print("Last index:", pandoraBox[-1])
print("Second last index:", pandoraBox[-2])
print("Size of pandoraBox:", len(pandoraBox))
print("Is Math in the list:", "Math" in pandoraBox)
print("Is Science in the list:", "Science" in pandoraBox)

#slicing list
print("pandoraBox[2:3] - ", pandoraBox[2:3])
print()

#list mutation (mutability)
print("Org:", pandoraBox)
pandoraBox[1] = "Geography"
print("New:", pandoraBox)

