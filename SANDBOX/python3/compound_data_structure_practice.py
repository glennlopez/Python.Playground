
# dictionary inside a dictionary
elements = \
    {
        # first layer
        'hydrogen': {
                        # second layer
                        'number': 1,
                        'weight': 1.008,
                        'symbol': 'H'
                    },

        # first layer
        'helium':   {
                        # second layer
                        'number': 2,
                        'weight': 4.003,
                        'symbol': 'He'
                    }

    }

try:
    print(elements['hydrogen']['weights'])
except KeyError:
    print("Does not exist.")

print()

# adding a new dictionary in elements
oxygen = \
    {
        'number': 8,
        'weight': 15.999,
        'symbol': "O"
    }

elements["oxygen"] = oxygen

# adding a key: value
elements["oxygen"]["isNoble"] = True

# print out
for key, value in elements.items():
    print(key, "=", value)


