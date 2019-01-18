#!/usr/bin/env python
x = input('How many Boxes? ')
message = raw_input('Type a message: ')

storage = []
for item in range(0,x):
	storage.append([message])

print storage