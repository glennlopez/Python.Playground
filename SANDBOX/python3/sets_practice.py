# https://www.youtube.com/watch?v=sBvaPopWOmQ

numbers = [8, 1, 2, 3, 1, 2, 3, 5, 8, 0, 9]
my_set = set(numbers)
print(my_set)
print(82 in my_set)

names = ["Glenn", "Lopez", "Glenn", "Gonazalez", "Burito"]
#names.append("pee")
my_name_set = set(names)
#names.append("poop")
print(my_name_set)

my_name_set.add("test")
print(my_name_set)

my_name_set.pop()
print(my_name_set)

sorted_set = sorted(my_name_set)
print(sorted_set)