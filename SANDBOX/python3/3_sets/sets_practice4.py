'''
Usecase 1:
    - Converting a ist to set to get rid of duplicates
'''

random_list = [1, 2, 3, 2, 54, 4, 3, 1, 'g', 'a', 'g', 3]
filter_list = {'n', 2, 'a', 'f'}

print(random_list, type(random_list))
unique_set = set(random_list)
print(unique_set, type(unique_set))

unique_set.add(200)
print(unique_set)

print(filter_list | unique_set)     # combine both set and show unique items
print(filter_list & unique_set)     # combine both set but only show items that both sets have
print(filter_list - unique_set)     # show the diff between both sets
print(filter_list ^ unique_set)     # returns items that does not exist in both sets

if 'z' in random_list:
    print('z is in random_list')
else:
    print('z is not in random_list')