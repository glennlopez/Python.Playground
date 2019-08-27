
primes = [2,3,5,7,11,15]

print(primes[1])
primes.append(17)
primes.append(19)
print(primes)

# index wrapping
wrap_test = [1,2,3]
print(wrap_test[-2])

# slicing
print(primes[0:2])

# lists within a list
list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', list_1]

print("list_2: " + str(list_2))
print("list_2[3][0]: " + str(list_2[3][0]))

