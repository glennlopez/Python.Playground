'''
https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/5a45f230-6087-4d0e-9e1a-3ddd4fc664e3
'''

points = 174  # use this input to make your submission
prize_name = "[default_value]"
no_prize = 0

# write your if statement here
if points <= 50:
    prize_name = "wooden rabbit"
elif 51 <= points <= 150:
    no_prize = 1
elif 151 <= points <= 180:
    prize_name = "wafer-thin mint"
elif 181 <= points <= 200:
    prize_name = "penguin"
else:
    no_prize = 1


if no_prize == 0:
    result = "Congratulations! You won a " + prize_name + "!"
else:
    result = "Oh dear, no prize this time."


print(result)