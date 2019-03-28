# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {
    "Shanghai": 17.8,
    "Istanbul": 13.3,
    "Karachi": 13.0,
    "Mumbai": 12.5
}

print("Russia" in population)

try:
    print(population["Russia"])
except KeyError:
    print("Russia not found!")

print("Population: " + str(population))

# get() method instead of population["Russia"]
print(population.get("Russia"))

# get() method with a default values
print(population.get("Russia", "Russia does not exist!"))

