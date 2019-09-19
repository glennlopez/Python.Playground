def party_planner(cookies, people):
    num_each = cookies // people
    leftovers = cookies % people

    return(num_each, leftovers)

num_each, leftover = party_planner(100,'g')
print("Number of cookies each: {}".format(num_each))
print("Number of cookies left: {}".format(leftover))

