'''
https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/c09059de-1e3a-4c06-9196-427250b29df5
'''
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
known_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]

for prime in check_prime:
    for i in range(len(known_prime)):                       # check number with known prime
        if prime % known_prime[i] == 0:                     # if number has remainder...
            print(prime, " is not a prime number.")             # is not a prime
            break                                               # ... then break from the loop
        if i == len(known_prime) - 1:                       # if end of the list of known prime is reached without breaking
            print(prime, " is a prime number.")             # then it is a prime
            known_prime.append(prime)                       # add the known prime to the list of know prime