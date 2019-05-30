#https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/788a3fa5-e1be-41ba-aab4-afad0a60b23b
"""
Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,'
to each dictionary in the elements dictionary.

After inserting the new entries you should be able to perform these lookups:
"""

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

for key, value in elements.items():
    print(key, '=', value)

print()

# Notes: you can use either-or but its easier to use the latter.
# Notice how python adds the 'key' in the element for you if it does not exist in the latter solution

elements['hydrogen'] = \
        {
            'number': 1,
            'weight': 1.00794,
            'symbol': 'H',
            'is_noble_gas': False
        }

elements['helium']['is_noble_gas'] = True

print()

for key, value in elements.items():
    print(key, '=', value)

