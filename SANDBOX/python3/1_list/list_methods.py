"""
# python list
my_mix_list = ["Glenn", "Lopez", 1987, 3, 24, "A0123DEF"]

my_string_list_1 = ["Glenn", "Lopez"]
my_string_list_2 = ["ABC", "abc"]
my_string_list_3 = ["abc", "ABC"]
my_string_list_4 = ["ZHD","AB", "ABC"]
my_string_list_5 = ["Z", "A", "S", "B"]

my_int_list_1 = [1, 34, 50, 12, 6, 5]

# TODO change the item only
print("String Length: " + str(len(my_mix_list)))
print("Max(): " + str(max(my_int_list_1)))
print("Min(): " + str(min(my_int_list_1)))
print("Sorted(): " + str(sorted(my_int_list_1)))
print("Sorted(): " + str(sorted(my_string_list_5)))
print("Sorted(): " + str(sorted(my_string_list_4)))
"""

# python list method

country = ["Canada", "Mexico", "America"]
name = ["Bob", "Nancy", "Albert"]

country.append("".join([name[1][0:3], country[1][-3:]]))

print(country)
country.sort()
print(country)

"""
print(country[0])
print(name[0])

print("".join([name[0][0:3], country[0][-3:]]))
print("".join([name[1][0:3], country[1][-3:]]))
print("".join([name[2][0:3], country[2][-3:]]))
"""