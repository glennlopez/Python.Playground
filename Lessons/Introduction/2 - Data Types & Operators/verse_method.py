"""
Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.

What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?
"""


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
#print(verse)
test = "you this and that and also this you"
print()

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

lenVerse = len(verse)
print("Length of verse: {}".format(lenVerse))

findFirst = verse.find("and")
print("First occurrence of 'and': {}".format(findFirst))

findLast = verse.rfind("you")
print("Last occurrence of 'you': {}".format(findLast))

countYou = verse.count("you")
print("Count of 'you': {}".format(countYou))
