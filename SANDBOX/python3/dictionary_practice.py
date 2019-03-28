#https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/47a34480-110c-4cfa-be87-73278fc1a1e3

animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3, 4, 2, 8, 2, 4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]
           }

print(animals.get("dogs"))
print(type(animals.get("dogs")))

animals["dogs"] = 300

print(animals.get("dogs"))
print(animals.get("fish"))
