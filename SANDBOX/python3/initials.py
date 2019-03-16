string = input("Name: ")
initials = ""

for char in string:
    if char.isupper():
        initials += char
print(initials)

