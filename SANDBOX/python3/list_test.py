
# Various datatypes stored in one list
list_of_random_stuff = [1, 1.3, 'G', "text", False]

print(list_of_random_stuff[0])
print(list_of_random_stuff[3])

addthings = list_of_random_stuff[0] + list_of_random_stuff[1]
print(addthings)

addthins2 = list_of_random_stuff[2] + list_of_random_stuff[3]
print(addthins2)

list_of_random_stuff[2] = 2
print(list_of_random_stuff[2])
addthins3 = list_of_random_stuff[0] + list_of_random_stuff[2]
print(addthins3)

list_size = len(list_of_random_stuff)
print("Size of list: {}".format(list_size))
print("Last item: {}".format(list_of_random_stuff[list_size - 1]))
print("Last item using -1: {}".format(list_of_random_stuff[-1]))