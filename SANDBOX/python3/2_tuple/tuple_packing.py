'''
Create a tuple function containing getting username and email using tuple unpacking
and return the tuple 

username: <prompt user>
email: <prompt user>
'''


def collect_user_data():
    username = input('Enter Username: ')
    email = input('Enter Email: ')
    return username, email                  # return multiple variables


signup_data = collect_user_data()           # collect data using function that returned multi-variables
user_username, user_email = signup_data     # un-pack tuple into a new variable
print(signup_data, type(signup_data))       # signup_data is a tuple
print(user_email, type(user_email))         # user_email is a str
print(user_username, type(user_username))   # user_username is an str
