'''
https://classroom.udacity.com/courses/ud1110/lessons/49912e64-4fe1-4f06-8679-d17d4ad33969/concepts/3487f6f7-ff59-40cf-8746-106c6bdca7a5
'''
# write your function here
def population_density(population, land_area):
    return population / land_area




# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))