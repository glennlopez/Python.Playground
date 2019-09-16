cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}
for cast_names, cast_heights in zip(cast_names, cast_heights):
    cast[cast_names] = cast_heights

print(cast)