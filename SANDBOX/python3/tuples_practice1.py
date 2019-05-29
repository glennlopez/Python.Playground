
# tuple example
my_tuple = (1, 2, 3, 4, 5)

for item in my_tuple:
    print(item)


print()
print("------------")
print()


# tuple practice
empty_tuple = ()
test1 = ("a",) # tuple with one element needs to have a coma
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1, type(test1))
print(test2, type(test2))
print(test3, type(test3))

print()

test_a = 1,
test_b = 1, 2
test_c = 1, 2, 3

print(test_a, type(test_a))
print(test_b, type(test_b))
print(test_c, type(test_c))

print()

# tuple assignment

player_1 = (100, "Glenn", True)
health, name, alive = player_1
name = ("test", )

print(player_1[1], type(player_1[1]))

