
starting = 0
ending = 20
current = starting
step = 6

while current < ending:
    if current + step > ending:
        # breaks out of loop if current next step is larger than ending
        break
    if current % 2:
        # skips the while loop if number is divisible by 2
        continue
    current += step
    print(current)
