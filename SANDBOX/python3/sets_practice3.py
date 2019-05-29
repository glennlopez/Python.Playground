example = set()

example.add(42)
example.add(False)
example.add(3.14)
example.add("Thorium")

print(example, type(example))
example.add(42)
example.add(41)
print(example)

example.remove(42)
print(example)

# example.remove(55)
example.discard(50)
print(example)
print()

# union and intersection
set1 = set([8, 2, 3, "a", "g", "c"])
set2 = set([1, 4, 3, "z", "b", "c"])
print(set1, type(set1))
print(set2, type(set2))
print()
print(set1.union(set2))
print(set1.intersection(set2))
print()
print(set2.union(set1))
print(set2.intersection(set1))