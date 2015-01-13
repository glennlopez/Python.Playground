'''
This is an example of how you can 
calculate wieghted avg mark using python
'''

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# function for average
def average(numbers):
    total = sum(numbers) #get add up all the numbers in the list
    total = float(total)
    total = total/len(numbers) #find the ammount of numbers in the list using len()
    return total
  
  #function for wieghed average mark  
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    # homework is 10%, quizzes: 30%, tests: 60%
    return homework*0.1 + quizzes*0.3 + tests*0.6