# creating tuples
school_subjects = ('math', 'science', 'geology', 'physics')
book = ("Enders Game", 1987, 'A', 98.2)

# accessing tuples
print(book[0])
print(school_subjects[1:3])

# updating tuples
update_1 = ("Glenn", )
book_update_1 = book + update_1

print(book_update_1)

# deleting tuple elements
school_subject_new = []
new_school_subject_tuple = ()
for item in school_subjects:
    if item != 'geology':
        school_subject_new.append(item)

new_school_subject_tuple = school_subject_new

print(new_school_subject_tuple, type(new_school_subject_tuple))

# NOTE: tuples cannot be updated or deleted

