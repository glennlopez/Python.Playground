# list
fruit = ['apple', 'orange', 'grapes', 'tomato']
rotten_fruits = ['mango']


for fruits in fruit:
    print(fruits)

# using range(start, stop, step)
for i in range(3):
    print("hello world")

# using range(start, stop, step)
for i in range(2, 11, 2):
    print(i)

print()
for item in rotten_fruits:
    print(item)
print()

for fruits in fruit:
    rotten_fruits.append(fruits.title())

print()
for item in rotten_fruits:
    print(item)
print()