'''
https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/f04a1bda-b2cd-420c-a25d-6e719a268c32
label: x, y, z
'''

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for x_coord, y_coord, z_coord, labels in zip(x_coord, y_coord, z_coord, labels):
    points.append("{}: {}, {}, {}".format(labels, x_coord, y_coord, z_coord))


for point in points:
    print(point)
