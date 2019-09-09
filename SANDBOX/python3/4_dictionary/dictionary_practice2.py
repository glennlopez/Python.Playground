a = {"Name": "Glenn", "DOB": 1987}
b = []
c = ()
d = {0, 1}
print(type(a))
print(type(b))
print(type(c))
print(type(d))

myDict = {}
print(myDict)

myDict["Name"] = "Glenn"
myDict["DOB"] = 1987
myDict["Age"] = 2019 - myDict["DOB"]
print(myDict)


# person = {0: {"name": "Glenn", "year": 1987, "month": 3, "day": 24}}

def get_data():
    name = input("What is your name: ")
    year = input("What year were you born: ")
    month = input("What month were you born: ")
    day = input("What day were you born: ")
    return name, int(year), int(month), int(day)


contact_info = get_data()
usr_name, usr_dob_year, usr_dob_month, usr_dob_day = contact_info
person = {0: {"name": usr_name, "year": usr_dob_year, "month": usr_dob_month, "day": usr_dob_day}}

print(person[0]["name"], "is", 2019 - person[0]["year"])
