# zipping lists together
first_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
second_list = [1, 2, 3, 4, 5]

for first_list, second_list in zip(first_list, second_list):
    print("{}: {}".format(first_list, second_list))

print()

# unzipping a list
fruits = [('apple', 2), ('orange', 4), ('grapes', 200)]
print(fruits)


fruit_name, ammount = zip(*fruits)
print(fruit_name)
print(ammount)