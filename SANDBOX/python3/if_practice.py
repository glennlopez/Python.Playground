
# basic
my_money = 100

if my_money < 10:
    print("Broke")
else:
    print("Not Broke")

# compound conditionals
age = 2
iq = 160
gender = "female"

if age < 18 and iq > 115:
    print("so smart")
elif age < 18 and iq > 115 and gender == "female":
    print("so smart girl")
else:
    print("smart")

