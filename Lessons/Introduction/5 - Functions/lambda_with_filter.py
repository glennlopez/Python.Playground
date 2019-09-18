# Link: https://classroom.udacity.com/courses/ud1110/lessons/49912e64-4fe1-4f06-8679-d17d4ad33969/concepts/9330654f-fbd0-4c90-bb30-cc0cb3b0a078
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)