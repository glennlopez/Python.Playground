import sys

# Wrong: Print everything in the argument
''' 
if len(sys.argv) > 1:
    for i in sys.argv:
        print(f"{sys.argv[i]}")
'''

# Correct: Print everything in the argument
'''
for s in sys.argv:
    print(s)
'''

# Print every character in the argument
'''
for string in sys.argv:
    for char in string:
        print(char)
'''
for s in sys.argv:
    for c in s:
        print(c)