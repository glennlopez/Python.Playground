#https://classroom.udacity.com/courses/ud1110/lessons/c06382b2-cb27-4aac-a2bd-eb754fd13914/concepts/9f46a018-d86f-4942-83d9-61abf2a9871e

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Jun - Sep
summer = month[5:9]
winter = month[9:12] + month[0:5]
target_month = "Jun"

print(summer)
print(winter)
print("{} is in summer: {}".format(target_month, target_month in summer))