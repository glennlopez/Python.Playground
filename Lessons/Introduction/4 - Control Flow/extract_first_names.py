'''
https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/be839dbf-f02a-4a51-b708-8e54f4b4f7e6
'''

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

