# iterable list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for letter in letters:
    print(letter)

print()

for i in range(0, 7, 2):  # odd letter only
    print(letters[i])

print()

for i in range(0, 4):
    print(letters[i])

# create a list using for-loop
new_letters = []
number_of_letters = input('How many letters to add: ')

for i in range(int(number_of_letters)):
    new_letters.append(input('Add letter: '))

print(new_letters)

# modify a list using a for loop - capitalize the letters
for i in range(len(new_letters)):
    new_letters[i] = new_letters[i].capitalize()

print(new_letters)