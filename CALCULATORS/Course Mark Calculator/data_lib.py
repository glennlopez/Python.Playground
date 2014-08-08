#!/usr/bin/env python

# Generate list from txt file
tests = []
with open('test.txt') as inputfile:
	for nums in inputfile:
		tests.append(nums)

# Converts string to intiger
tests = map(int, nums.split(","))

