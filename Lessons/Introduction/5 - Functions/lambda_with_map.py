'''
https://classroom.udacity.com/courses/ud1110/lessons/49912e64-4fe1-4f06-8679-d17d4ad33969/concepts/9330654f-fbd0-4c90-bb30-cc0cb3b0a078
'''
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)