def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

num_each, leftover = party_planner(100,0)
print("Number of cookies each: {}".format(num_each))
print("Number of cookies left: {}".format(leftover))

