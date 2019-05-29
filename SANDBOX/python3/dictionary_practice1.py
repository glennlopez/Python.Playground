
car = {"Make": "Nissan", "Model": "Ultima", "Year": 1992, "isNew": False}

for item in car:
    print(item)

print(type(car))

print()
print()


animal = dict(type="Dog", age=4)
print(animal, type(animal))

# add: key value pair to animal
animal["Trained"] = True

print(animal)
print("Trained: " + str(animal['Trained']))
print()

for item in animal.keys():
    value = animal[item]
    print(item, "=", value)


