long_str = '''In this tutorial, learn how to iterate through python string. 
You can loop through string variable in Python with for loop or while loop. 
Use direct string to loop over string in Python'''

# temp list for storing lower case long_str
lowercase_long_str = []

for i in range(len(long_str)):
    if long_str[i].isalpha():
        lowercase_long_str.append(long_str[i].lower())

# stores counted letters and spaces
letter_frq = {}

for char in lowercase_long_str:
    if char not in letter_frq:
        letter_frq[char] = 1
    else:
        letter_frq[char] += 1

print(letter_frq)